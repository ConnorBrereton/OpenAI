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
Stay calm for a little (breathe) \ 
'Til you find me \ 
Let's meet in the middle (breathe) \ 
Run your hands up and down me \ 
And I've been on your mind (breathe) \ 
Haven't I lately? \ 
And you've been trying to fight (breathe) \ 
Whatever you're feeling, feeling \ 
Let me show you what it means to be human \ 
To be wanted, to be vulnerable \ 
Let me show you what it means to be human \ 
To be helpless, and emotional \ 
Let me show you what it means to be human \ 
Whatever you want to do with me \ 
What it means to be human \ 
Let me show you what it means to be human \ 
Let me show you what it means to be human \ 
Whatever you want to do with me \ 
What it means to be human \ 
"""

# This is a real product.
prompt = f"""
Identity the emotions of the following song lyrics \ 
Lyrics: ```{text}``` that the writer wrote.

Expresss the emotions in no more than 4 words.

Format the answer as a list of emotions separated by commas.

The answer has to be no more than 4 words ordered by the \ 
strongest emotions first.
"""

response = get_completion(prompt)
print(response)