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
Riding a Santa Cruz mountain bike in the Marin woods. 
"""

# This is a real product.
prompt = f"""
Translate the following text to Spanish, German, and English Pirate.

Format like this:

English: . . .
Spanish: . . .
German: . . .
English Pirate: . . .

```{text}```
"""

response = get_completion(prompt)
print(response)