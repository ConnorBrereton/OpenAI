import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# Set OpenAI API key
openai.api_key=os.getenv('OPENAI_API_KEY')

# Set the API endpoint and prompt
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


text = f"""
"""

prompt = f"""
Your task is to determine if the developer's solution \
is correct or not.
To solve the problem do the following:
- First, work out your own solution to the problem. 
- Then compare your solution to the developer's solution \ 
and evaluate if the developer's solution is correct or not. 
Don't decide if the developer's solution is correct until 
you have done the problem yourself.

Use the following format:
Question:
```
question here
```
Developer's solution:
```
developer's solution here
```
Actual solution:
```
steps to work out the solution and your solution here
```
Is the developer's solution the same as actual solution \
just calculated:
```
yes or no
```
Developer grade:
```
correct or incorrect
```

Question:
```
I'm building a solar power installation and I need help \
working out the financials. 
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot
- I negotiated a contract for maintenance that will cost \
me a flat $100k per year, and an additional $10 / square \
foot
What is the total cost for the first year of operations \
as a function of the number of square feet.
``` 
Developer's solution:
```
Let x be the size of the installation in square feet.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
```
Actual solution:
"""

response = get_completion(prompt)
print(response)