from openai import OpenAI

def ChatGPT():
    return OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)
def generate_linkedin_post(prompt):
    client = ChatGPT()
    completion = client.chat.completions.create(
    model="meta-llama/llama-3.3-8b-instruct:free",
    messages=[
    {
      "role": "user",
      "content": prompt
    }
  ]
)
    return completion.choices[0].message.content
