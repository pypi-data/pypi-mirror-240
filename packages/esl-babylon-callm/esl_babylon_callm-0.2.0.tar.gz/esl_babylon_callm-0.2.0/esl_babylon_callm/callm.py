import abc
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import redis
from langchain.callbacks import get_openai_callback, FileCallbackHandler, OpenAICallbackHandler
from langchain.chains import LLMChain
from langchain.chat_models import AzureChatOpenAI
from langchain.memory import ConversationBufferMemory, ReadOnlySharedMemory
from langchain.prompts import PromptTemplate
from langchain.tools import BaseTool
from pydantic import BaseModel, constr, conint
from sqlalchemy.orm import Session

from esl_babylon_callm.utils.get_memory import get_memory
from esl_babylon_callm.utils.get_prompt_template import get_prompt_template
from esl_babylon_callm.utils.logger.create_logger import logger
from esl_babylon_callm.utils.logger.formatter import Colors


class ChatRequest(BaseModel):
    message: constr(strip_whitespace=True, min_length=1) = "default_message"
    username: constr(strip_whitespace=True, min_length=1) = "default_username"
    enterprise_id: conint(ge=0) = 0
    simulation_id: conint(ge=0) = 0


class CaLLM:
    __slots__ = ["llm",
                 "db_session",
                 "chat_request",
                 "tool_list",
                 "name",
                 "description",
                 "url",
                 "memory",
                 "data_path"]

    llm: AzureChatOpenAI
    db_session: Session | None
    chat_request: ChatRequest
    tool_list: dict[str, BaseTool]
    name: str
    description: str
    url: str
    memory: ConversationBufferMemory
    data_path: Path

    default_input = "Introduce yourself to the User, explain the rules of the conversation with you."
    user_string = f"{Colors.DEBUG}\nINPUT:\n{Colors.RESET}"
    assistant_string = f"{Colors.DEBUG}\nLLM_OUTPUT:\n{Colors.RESET}"

    def __init__(self,
                 deployment_name: str,
                 openai_api_type: str,
                 openai_api_version: str,
                 openai_api_key: str,
                 openai_api_base: str,
                 temperature: float,
                 db_session: Session | None,
                 chat_request: ChatRequest,
                 tool_list: list | None,
                 name: str,
                 description: str,
                 url: str,
                 data_path: Path) -> None:
        self.llm = self.get_llm(deployment_name=deployment_name,
                                openai_api_type=openai_api_type,
                                openai_api_version=openai_api_version,
                                openai_api_key=openai_api_key,
                                openai_api_base=openai_api_base,
                                temperature=temperature)
        self.db_session = db_session
        self.chat_request = chat_request
        if tool_list is None:
            tool_list = []
        self.tool_list = {tool.name: tool for tool in tool_list}
        self.name = name
        self.description = description
        session_id = f"{chat_request.enterprise_id}_{chat_request.username}_{chat_request.simulation_id}_{name}"
        self.url = url
        self.memory = get_memory(session_id=session_id, url=url)
        self.data_path = data_path

    @abc.abstractmethod
    def run(self, *args, **kwargs) -> Any:
        raise NotImplementedError

    def get_assistant_reply(self,
                            template_format: str,
                            hash_dir_name: str | None = None,
                            add_memory: bool = False,
                            **kwargs) -> str:
        user_input_key = "user_input"
        if user_input_key in kwargs:
            user_input = kwargs.get(user_input_key, self.default_input)
            self.memory.chat_memory.add_user_message(message=user_input)
            logger.info(f"{self.user_string}{user_input}")
        prompt_template = get_prompt_template(template_format=template_format)
        dir_name = hash_dir_name if hash_dir_name else f"{datetime.now().strftime('%Y-%b-%d %H-%M-%S-%f')}"
        dir_path = self.data_path / dir_name
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
        chain = self.get_chain(prompt_template=prompt_template, dir_path=dir_path, add_memory=add_memory)
        with get_openai_callback() as open_ai_cb:
            start_time = time.time()
            response_received = False
            while not response_received:
                try:
                    assistant_reply = chain.run(**kwargs)
                    response_received = True
                except Exception as e:
                    logger.error(e)
            execution_time = time.time() - start_time
            self.aggregate_llm_data(deployment_name=chain.llm.deployment_name,
                                    total_tokens=open_ai_cb.total_tokens,
                                    prompt_tokens=open_ai_cb.prompt_tokens,
                                    completion_tokens=open_ai_cb.completion_tokens,
                                    successful_requests=open_ai_cb.successful_requests)
            assistant_reply = self.write_assistant_reply(assistant_reply=assistant_reply,
                                                         dir_path=dir_path,
                                                         execution_time=execution_time,
                                                         open_ai_cb=open_ai_cb)
        self.memory.chat_memory.add_ai_message(assistant_reply)
        logger.info(f"{self.assistant_string}{assistant_reply}")
        return assistant_reply

    def get_chain(self,
                  prompt_template: PromptTemplate,
                  dir_path: Path,
                  add_memory: bool = False,
                  verbose: bool = False) -> LLMChain:
        memory = ReadOnlySharedMemory(self.memory) if add_memory else None
        dir_path = dir_path / "prompt.txt"

        chain = LLMChain(llm=self.llm,
                         prompt=prompt_template,
                         memory=memory,
                         verbose=verbose,
                         callbacks=[FileCallbackHandler(dir_path)])
        return chain

    @staticmethod
    def write_assistant_reply(assistant_reply: str,
                              dir_path: Path,
                              execution_time: float,
                              open_ai_cb: OpenAICallbackHandler) -> str:
        dir_path = dir_path / "output.txt"
        data = f"""
        \n
        Execution time: {execution_time}s
        Total tokens: {open_ai_cb.total_tokens}
        Prompt tokens: {open_ai_cb.prompt_tokens}
        Completion tokens: {open_ai_cb.completion_tokens}
        Successful requests: {open_ai_cb.successful_requests}
        Total cost: {open_ai_cb.total_cost}
        """

        augmented_reply = assistant_reply + data
        with open(dir_path, 'w+') as file:
            file.write(augmented_reply)

        return assistant_reply

    @staticmethod
    def get_llm(deployment_name: str,
                openai_api_type: str,
                openai_api_version: str,
                openai_api_key: str,
                openai_api_base: str,
                temperature: float) -> AzureChatOpenAI:
        llm = AzureChatOpenAI(deployment_name=deployment_name,
                              openai_api_type=openai_api_type,
                              openai_api_version=openai_api_version,
                              openai_api_key=openai_api_key,
                              openai_api_base=openai_api_base,
                              temperature=temperature)
        return llm

    def aggregate_llm_data(self, deployment_name: str, **kwargs) -> None:
        try:
            r = redis.StrictRedis.from_url(url=self.url, decode_responses=True)
            for key, value in kwargs.items():
                redis_key = f"{deployment_name}"
                r.hincrby(redis_key, key, int(value))
        except Exception as e:
            return logger.error(e)
