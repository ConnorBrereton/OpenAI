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
The meaning of life is a philosophical and existential question that has been debated by scholars, \ 
thinkers, and individuals throughout history. There is no one definitive answer to this question, \ 
as it can be interpreted in many different ways depending on one's beliefs, values, and experiences. \ 
Some people believe that the meaning of life is to pursue happiness, others believe it is to fulfill \ 
a specific purpose or destiny, and still others believe that life has no inherent meaning and that \ 
we must create our own meaning through our experiences and interactions with the world around us. \ 
Ultimately, the meaning of life is a deeply personal and subjective concept that can only be \ 
defined by each individual for themselves.
"""

prompt = f"""
Perform the following actions: 
1 - Summarize the following text delimited by triple \
backticks with 1 sentence.
2 - Translate each verb in the text into French.
3 - List each verb in the French summary.
4 - Output a json object that contains the following \
keys: french_summary, num_verbs.

Separate your answers with line breaks.

Text:
```{text}```
"""

response = get_completion(prompt)
print(response)