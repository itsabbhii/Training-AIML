import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")
while True:
    request = input("Enter your request: ")
    if request=="exit":
        break
    response = model.generate_content(request)
    print(response.text)
