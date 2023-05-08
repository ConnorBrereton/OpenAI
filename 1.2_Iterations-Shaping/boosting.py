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
Model: Santa Cruz Tallboy 4

Frame Material: Carbon fiber or aluminum (depending on build kit)

Frame Suspension: VPP (Virtual Pivot Point) suspension design with 120mm (4.7 inches) of travel

Fork: Fox 34 or 36 (depending on build kit) with 130mm (5.1 inches) of travel

Rear Shock: Fox Float Performance DPS or DPX2 (depending on build kit)

Wheels: 29-inch diameter

Tires: Maxxis Minion DHR II (rear) and Maxxis Minion DHF (front) tires

Brakes: Shimano or SRAM hydraulic disc brakes (depending on build kit)

Drivetrain: Shimano or SRAM 1x11 or 1x12 (depending on build kit)

Handlebar: Santa Cruz carbon or aluminum handlebar (depending on build kit)

Stem: RaceFace or Santa Cruz stem (depending on build kit)

Seatpost: RockShox Reverb or Fox Transfer dropper seatpost (depending on build kit)

Saddle: WTB or Santa Cruz saddle (depending on build kit)

Weight: Carbon fiber frame models weigh approximately 2.7 kg (6 lbs) and aluminum frame models weigh approximately 3.4 kg (7.5 lbs) without pedals.

Other Features:

Boost spacing on front and rear hubs for increased wheel stiffness and strength
Threaded bottom bracket for easy maintenance
Internal cable routing for a clean look and protection from the elements
Compatible with 1x or 2x drivetrains
Available in multiple colors and build kits to suit different riding styles and preferences.
"""

# This is a real product.
prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

The description is intended for advanced riders, 
so should be technical in nature and focus on the 
materials the product is constructed from.

At the end of the description, include every 7-character 
Product ID in the technical specification.

Technical specifications: ```{text}```
"""

response = get_completion(prompt)
print(response)