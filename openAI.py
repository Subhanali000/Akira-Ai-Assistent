
import openai

# Replace with your actual API key
openai.api_key = "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"

response = openai.Completion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are Virtual Assistant named AKIRA, skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(response.choices[0].message["content"])


