import openai
import json

openai.api_key = "<please ask for api-key or generate a new one>"

# Define a list of questions
questions = [
  "How much do you want to invest?",
  "Which company mutual funds are you looking for?",
  "What is your investment time horizon? (e.g. 1-3 years, 5+ years etc. Give value/range in years)",
  "What is your risk tolerance? (high/moderate/low)",
  "what is your age? (in years)",
  "What is your investment objective? (e.g. retirement, Growth, Income, or Preservation etc.)"
  # Add more questions as needed
]

# Collect user answers
answers = {}
for question in questions:
  user_input = input(question + " ")
  answers[question] = user_input

# Generate mutual fund recommendations based on user answers
prompt = f"I want to invest {answers['How much do you want to invest?']} in mutual fund of {answers['Which company mutual funds are you looking for?']} in 2023 with {answers['What is your risk tolerance? (high/moderate/low)']} risk and high returns for {answers['What is your investment time horizon? (e.g. 1-3 years, 5+ years etc. Give value/range in years)']} years. My age is {answers['what is your age? (in years)']} years. Investment objective is {answers['What is your investment objective? (e.g. retirement, Growth, Income, or Preservation etc.)']}."

print('Customer Query is: ',prompt)
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  max_tokens=3000,
  n=1,
  stop=None,
  temperature=0.3,
)

# params={
#   "engine": "text-davinci-002",
#   "prompt": prompt,
#   "temperature": 0.4,
#   "max_tokens": 3000,
#   "n": 1,
#   "stop": None
# }

# Print the recommended mutual funds
print(response.choices[0].text)

# # Call the OpenAI API to generate a response
# response = openai.Completion.create(**params)

# # Parse the response and extract the recommended mutual funds
# output = response.choices[0].text.strip()
# output = json.loads(output)
# mutual_funds = output["data"]

# # Print the recommended mutual funds
# print("Here are some mutual funds that may be a good fit for your investment goals:")
# for fund in mutual_funds:
#     print("- {}".format(fund))
