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
What is the capital of France? The capital of France is Paris. \ 
What is the square root of 64? The square root of 64 is 8. \ 
What is the difference between a virus and a bacteria? \ 
Viruses and bacteria are both types of microorganisms that can cause illness, \ 
but they differ in several ways. For example, viruses require a host cell to reproduce, \ 
while bacteria can reproduce on their own. Additionally, antibiotics are effective \ 
against bacteria, but not viruses. How do I cook a steak? There are many ways to \ 
cook a steak, but one popular method is to sear it in a hot pan and then finish it \ 
in the oven. The basic steps are to preheat your oven to 400°F (204°C), season your \ 
steak with salt and pepper, heat a heavy, oven-safe skillet (such as a cast iron skillet) \ 
over high heat until it is very hot, add a tablespoon of oil to the skillet and swirl it \ 
around to coat the bottom, carefully add the steak to the skillet and let it sear for 2-3 \ 
minutes on each side, transfer the skillet to the preheated oven and cook the steak for an \ 
additional 4-6 minutes, until it reaches your desired level of doneness (use a meat \ 
thermometer to check the internal temperature), and remove the skillet from the oven and \ 
let the steak rest for a few minutes before slicing and serving. What is the meaning of life? \ 
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
You will be provided with text delimited by triple quotes. 
If it contains a question with an answer to the question, \ 
re-write those questions and answers in the following format:

Question 1 - ...
Answer 1 - …
Question 2 - ...
Answer 2 - …
…
Question N - ...
Answer N - …

If the text does not contain a question or answer, \ 
then simply write \"No Q&A provided provided.\"

\"\"\"{text}\"\"\"
"""

response = get_completion(prompt)
print(response)