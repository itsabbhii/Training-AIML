import google.generativeai as genai

genai.configure(api_key="AIzaSyDs-ZaxYcrgAKNVIzbbfSU74VoYTT0PwrQ")

model = genai.GenerativeModel("gemini-1.5-flash")

request = input("Enter your request")
response = model.generate_content(request)
print(response.text)
