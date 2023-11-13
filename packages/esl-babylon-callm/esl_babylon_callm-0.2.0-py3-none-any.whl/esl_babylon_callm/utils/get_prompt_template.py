from langchain.prompts import PromptTemplate


def get_prompt_template(template_format: str) -> PromptTemplate:
    prompt_template = PromptTemplate.from_template(template_format=template_format)
    return prompt_template
