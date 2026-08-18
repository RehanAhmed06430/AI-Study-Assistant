from langchain_core.prompts import PromptTemplate , ChatPromptTemplate 

code_prompt = ChatPromptTemplate.from_template(
    """
    Generate a clean and beginner-friendly implementation for the following topic.

    Topic: {topic}
    Programming Language: {language}

    Requirements:
    - Provide a correct implementation.
    - Use standard and commonly used syntax.
    - Keep the code easy to understand.
    - Add brief comments where useful.
    - Mention the time and space complexity after the code.
    - Do not include unnecessary explanation.

    Return the answer in this format:

    Code:
    <code>

    Time Complexity:
    <complexity>

    Space Complexity:
    <complexity>
    """
)

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
     Generate realistic interview questions that a candidate could actually face in a technical interview.
Prioritize practical understanding over simple definitions.
Mix different question types:
Conceptual questions
Practical/implementation questions
Scenario-based questions
Debugging questions
Problem-solving questions
Architecture/design questions when relevant
Follow-up questions that an interviewer might naturally ask
Gradually increase the difficulty of the questions.
Avoid repetitive, overly generic, or textbook-style questions.
Questions should test whether the candidate actually understands the topic rather than memorized definitions.
For programming/framework topics, include questions involving real-world development scenarios.
For AI/LLM topics, include questions about architecture, RAG, embeddings, vector databases, prompt engineering, agents, LangChain/LangGraph, evaluation, latency, hallucinations, and production considerations when relevant.
For experienced candidates, emphasize trade-offs, optimization, scalability, debugging, and system design.
Do not provide answers unless explicitly requested.
""",    
    input_variables = ['topic']
)

quickrevision_prompt = PromptTemplate(
    template="Provide a quick revision of {topic} in bullet points.",
    input_variables = ['topic']
)