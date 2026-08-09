from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    template = "Explain {topic} in simple language.",
    input_variables = ['topic']
)