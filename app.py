from models import model
topic = "Binary Search"
response = model.invoke(
    f"Explain {topic} in simple language."
)

print(response.content)