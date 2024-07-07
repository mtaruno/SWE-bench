from zhipuai import ZhipuAI
client = ZhipuAI(api_key="c61773dce745c19e8f36a739667d3f03.itPVpSuSrNf1YsyQ") # Fill in your own APIKey
response = client.chat.completions.create(
  model="glm-4",  # Fill in the model name to be called
  messages=[
      {"role": "user", "content": "As a marketing expert, please create an attractive slogan for my product"},
      {"role": "assistant", "content": "Of course, to create an attractive slogan, please tell me some information about your product"},
      {"role": "user", "content": "ZhipuAI Open Platform"},
      {"role": "assistant", "content": "Empowering the future, mapping infinity - ZhipuAI, making innovation accessible!"},
      {"role": "user", "content": "Create a more accurate and attractive slogan"}
  ],
)
print(response.choices[0].message)