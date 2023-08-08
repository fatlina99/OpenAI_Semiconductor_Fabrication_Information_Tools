# Semiconductor Fabrication Information Tool

#%%
## Import Libraries

import os
import openai
from dotenv import load_dotenv

#%%
# Run OpenAI API KEY
load_dotenv()
openai.api_key = os.getenv("API_KEY")

#%%
## Tools

# Keywords related to semiconductor fabrication
allowed_keywords = ["semiconductor", "fabrication", "wafer", "doping", "etching", "deposition", "lithography", "oxide",
                    "diffusion", "ion", "implanter", "cleanroom", "photomask", "photoresist", "exposure",
                    "development", "ion-implant", "annealing", "polysilicon", "thin-film", "dry-etch", "wet-etch",
                    "chemical-mechanical polishing", "CMP", "thermal oxidation", "dielectric", "interconnect", "contact",
                    "via", "CMOS", "IC", "transistor", "diode", "capacitor", "resistor", "process", "yield", "substrate",
                    "ion implantation", "photolithography", "interconnect", "packaging", "microelectronics", "MEMS", "E-beam",
                    "CVD", "PVD", "GaN", "silicon", "manufacturing", "mask", "photresist", "ion milling", "plasma etching",
                    "chemical vapor deposition", "physical vapor deposition", "chemical mechanical planarization", "wafer bonding",
                    "back-end-of-line", "front-end-of-line", "FET", "metallization", "P-Mosfet", "N-Mosfet", "yellow room", "re-work"]

#%%
def input_tool(msg):
  # Check if the user input contains keywords related to semiconductor fabrication
    if not any(keyword in msg.lower() for keyword in allowed_keywords):
        print("Sorry, the tool is designed for semiconductor fabrication information only.")
        return

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                "role": "system",
                "content": "you are the best semiconductor engineer, explain the answer accurately, the explanation needs to be easy to understand by a student, give an example if required"
            },
            {
                "role": "user",
                "content": msg
            },
            {
                "role": "user",
                "content": "Explain the concept."
            },
            {
                "role": "user",
                "content": ""
            },
            {
                "role": "user",
                "content": "Give an example if possible."
            }
        ],
        max_tokens=500,
        temperature=0.5
    )

    tools_output = response['choices'][0]['message']['content']
    print(tools_output)

#%%
# Call the function with the question
input_tool("In what room photolithography process was conducted yellow room?")

#%%
# Call the function with an input outside the semiconductor fabrication scope
input_tool("Netfix top 5 movies")


#%%