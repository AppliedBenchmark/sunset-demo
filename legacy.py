from openai import OpenAI
client = OpenAI()
resp = client.chat.completions.create(model="gpt-4-0314")
