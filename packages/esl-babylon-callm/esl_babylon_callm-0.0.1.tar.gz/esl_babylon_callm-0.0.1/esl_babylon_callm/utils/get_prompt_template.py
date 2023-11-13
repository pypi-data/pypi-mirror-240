from langchain.prompts import PromptTemplate


def get_prompt_template(template: str) -> PromptTemplate:
    prompt_template = PromptTemplate.from_template(template=template)
    return prompt_template
