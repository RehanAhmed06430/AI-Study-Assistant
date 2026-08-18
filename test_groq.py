from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("API key found:", api_key is not None)

if not api_key:
    print("❌ GROQ_API_KEY nahi mili")
    exit()

client = Groq(api_key=api_key)

try:
    models = client.models.list()

    print("✅ API key working!")
    print("\nAvailable models:")

    for model in models.data:
        print(model.id)

except Exception as e:
    print("❌ API key/API request failed:")
    print(e)