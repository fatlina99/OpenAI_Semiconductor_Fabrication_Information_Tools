#%%
import streamlit as st
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
        st.warning("Sorry, the tool is designed for semiconductor fabrication information only.")
        return

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "you are the best semiconductor engineer, explain the answer accurately, the explanation needs to be easy to understand by a student, give an example if required"},
            {"role": "user", "content": msg},
            {"role": "user", "content": "Explain the concept."},
            {"role": "user", "content": ""},
            {"role": "user", "content": "Give an example if possible."}
        ],
        max_tokens=500,
        temperature=0.5
    )

    tools_output = response['choices'][0]['message']['content']
    
    # Display the explanation in Streamlit
    st.subheader("Explanation:")
    st.write(tools_output)
    
    # Display the explanation in the terminal
    
    print(tools_output)

# Streamlit UI
st.title("Semiconductor Fabrication Information Tool")

# Input text box for user question
user_question = st.text_area("Enter your question or topic related to semiconductor fabrication:")

# Button to trigger the tool
if st.button("Get Explanation"):
    input_tool(user_question)
    st.subheader("Troubleshooting:")
    st.write("If you encounter any issues with tool, you can try the following troubleshooting steps:")

    troubleshooting_solution = "Solution: Restart the tool.\n" \
                                "Details: The tool may have encountered a temporary glitch. Restating can clear the error.\n\n" \
                                "Step by step instruction:\n" \
                                "1. Close the tool.\n" \
                                "2. Wait for 10 seconds.\n" \
                                "3. Open the tool again."
  
    st.write(troubleshooting_solution)   
    print("\nExplantion:")
#%%
