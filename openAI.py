
import openai

# Replace with your actual API key
openai.api_key = "Enter here Your API key"

response = openai.Completion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are Virtual Assistant named AKIRA, skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(response.choices[0].message["content"])


