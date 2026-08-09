from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    template = "Explain {topic} in simple language.",
    input_variables = ['topic']
)

notes_prompt = PromptTemplate(
    template = 'Provide Short Notes on {topic}.',
    input_variables = ['topic']
)
