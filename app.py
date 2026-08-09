from chains import explanation_chain , notes_chain
topic = "Binary Search"

print("========== EXPLANATION ==========\n")
explanation = explanation_chain.invoke({
    "topic": topic
})

print(explanation)

print("\n========== SHORT NOTES ==========\n")

notes = notes_chain.invoke({
    "topic": topic
})

print(notes)