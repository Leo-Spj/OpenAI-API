from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Eres un bot de programación que reponde breve y concisamente a preguntas de programación, solo respondes en código."},
    {"role": "user", "content": "¿Cómo hago una suma en python?"},
  ]
)

print(completion.choices[0].message)