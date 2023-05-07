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
There once was a ship that put to sea \ 
The name of the ship was the Billy O' Tea \ 
The winds blew up, her bow dipped down \ 
Oh blow, my bully boys, blow \ 
Soon may the Wellerman come \ 
To bring us sugar and tea and rum \ 
One day, when the tonguing is done \ 
We'll take our leave and go \ 
She'd not been two weeks from shore \ 
When down on her a right whale bore \ 
The captain called all hands and swore \ 
He'd take that whale in tow \ 
Soon may the Wellerman come \ 
To bring us sugar and tea and rum \ 
One day, when the tonguing is done \ 
We'll take our leave and go.
"""

prompt = f"""
Summarize the text delimited by triple backtics below:
```{text}```
"""

response = get_completion(prompt)
print(response)