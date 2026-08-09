from models import model
from prompts import explain_prompt, notes_prompt
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
explanation_chain = explain_prompt | model | parser
notes_chain = notes_prompt | model | parser