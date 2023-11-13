from langchain.memory import ConversationBufferMemory, RedisChatMessageHistory


def get_memory(session_id: str, url: str) -> ConversationBufferMemory:
    chat_memory = RedisChatMessageHistory(session_id=session_id, url=url, key_prefix="")
    memory = ConversationBufferMemory(chat_memory=chat_memory)
    return memory
