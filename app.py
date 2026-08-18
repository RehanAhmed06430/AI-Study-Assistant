from chains import study_chain
from dotenv import load_dotenv
load_dotenv()

topic = "Two Pointers"


result = study_chain.invoke({
    "topic": topic
})


print("\n========== EXPLANATION ==========\n")
print(result["explanation"])


print("\n========== SHORT NOTES ==========\n")
print(result["notes"])


print("\n========== INTERVIEW QUESTIONS ==========\n")
print(result["interview"]) 

print("\n========== QUICK REVISION ==========\n")
print(result["quickrevision"])
