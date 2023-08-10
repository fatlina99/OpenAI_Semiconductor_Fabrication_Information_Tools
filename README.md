# OpenAI_Semiconductor_Fabrication_Information_Tools
 
# Semiconductor Fabrication Information Tool

This tool provides information about methods, applications, and concepts in the field of semiconductors. It offers precise answers tailored to semiconductor-related queries. The tool is designed for students who have an interest in learning about semiconductors.


# Functionality
## User Inputs
 1. The user needs to input the description about wafer/semiconductor fabrication.
 2. The user needs to input the question or problem in wafer/semiconductor fabrication.
    
## Outputs
 1. The tool will output an answer,  solution, and information in the text.
 2. The tool will highlight relevant answers based on the latest technologies.
 3. Any question that is out of the semiconductor field will be not answered.

# Technologies:
 - Streamlit for deployment

# OpenAI Models:
 - GPT-3.5-turbo

# Code Explaintion

This Python script is designed to facilitate answering questions related to semiconductor fabrication processes using the OpenAI API and the GPT-3.5 model. It filters user input based on a predefined list of keywords related to semiconductor fabrication and generates informative responses in an easy-to-understand manner. Here's how the tool works:

 1. Import Libraries: The necessary libraries are imported, including `os`, `openai`, and `load_dotenv`.

 2. Load OpenAI API Key: The OpenAI API key is loaded from the environment using the `load_dotenv()` function.

 3. Define Allowed Keywords: The `allowed_keywords` list contains various keywords associated with semiconductor fabrication.

 4. `input_tool` Function: This function processes user input. If the input contains `allowed_keywords`, it sends a request to the OpenAI API for generating responses.
  - The model used is `gpt-3.5-turbo`.
  - The response includes a system prompt, user inputs, and requests for explanations and examples.
  - Response length is controlled using `max_tokens`, and response randomness is controlled using `temperature`.
Call the Function: The `input_tool` function is called twice to demonstrate its functionality with both semiconductor fabrication-related input and unrelated input.

To use this tool, ensure you have the required libraries installed (`openai`, `dotenv`) and set up your OpenAI API key as an environment variable. You can customize the `allowed keywords` according to your needs.

Feel free to modify and integrate this tool into your projects or applications!

![output_1](https://github.com/fatlina99/OpenAI_Semiconductor_Fabrication_Information_Tools/assets/141213373/0f3c5a5a-dabe-4413-bf2c-9139d6c708c6)

![output_2](https://github.com/fatlina99/OpenAI_Semiconductor_Fabrication_Information_Tools/assets/141213373/1f73d44a-8d4f-44c7-a18a-5ae38bf97ef6)



