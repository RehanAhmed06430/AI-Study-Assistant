from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    template = "Explain {topic} in simple language.",
    input_variables = ['topic']
)

notes_prompt = PromptTemplate(
    template = 'Provide Short Notes on {topic}.',
    input_variables = ['topic']
)

interview_prompt = PromptTemplate(
    template = """Provide Interview Question on {topic}.
    Generate 5 important interview questions.
    Do not provide answers.
    Only provide the questions.
    """,    
    input_variables = ['topic']
)
