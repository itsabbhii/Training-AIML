import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("OPENAI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

request = input("Enter your request")
response = model.generate_content(request)
print(response.text)
