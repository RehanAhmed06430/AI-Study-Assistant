from chains import study_chain
from dotenv import load_dotenv
load_dotenv()

topic = "Two Pointers"
language = "C++"

result = study_chain.invoke({
    "topic": topic,
    "language": language
})


print("\n========== EXPLANATION ==========\n")
print(result["explanation"])


print("\n========== SHORT NOTES ==========\n")
print(result["notes"])


print("\n========== INTERVIEW QUESTIONS ==========\n")
print(result["interview"]) 

print("\n========== QUICK REVISION ==========\n")
print(result["quickrevision"])

print("\n========== CODE IMPLEMENTATION ==========\n")
print(result["code"])