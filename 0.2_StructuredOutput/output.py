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
Generate a list of three names for a new \ 
startup company that is focused on cybersecurity \ 
that uses AI as a core part of its product offering. \ 
The company should be named after a Greek creature \ 
and only have one word in its name. \ 
Provide them in JSON format with the following keys: \ 
company_id, title, founder.
"""

prompt = f"""
Follow the instructions in the text delimited by triple backtics below:
```{text}```
"""

response = get_completion(prompt)
print(response)