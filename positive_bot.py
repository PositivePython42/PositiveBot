# PositiveBot v0.1 :: Sean Massey
# Please feel free to add feature requests, but please be positive!

import openai

openai.api_key = "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" # Replace with your API key

chatbot_input = input("What do you want to know today? ")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": chatbot_input
    }
  ],
  temperature=1,
  max_tokens=500,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response['choices'][0]['message']['content'])