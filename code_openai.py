from openai import OpenAI
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)


