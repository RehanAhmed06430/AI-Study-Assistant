from models import model
from prompts import explain_prompt, notes_prompt, interview_prompt, quickrevision_prompt, code_prompt   
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel 

parser = StrOutputParser()

explanation_chain = explain_prompt | model | parser
notes_chain = notes_prompt | model | parser
interview_chain = interview_prompt | model | parser
quickrevision_chain = quickrevision_prompt | model | parser
code_chain = code_prompt | model | parser

study_chain  = RunnableParallel({
    "explanation": explanation_chain,
    "notes": notes_chain,
    "interview": interview_chain,
    "quickrevision": quickrevision_chain,
    "code": code_chain
})