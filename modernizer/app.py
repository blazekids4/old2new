import json
import requests
from bs4 import BeautifulSoup
import base64
from openai import AzureOpenAI, OpenAI
from dotenv import load_dotenv
import os
from flask_cors import CORS
from flask import jsonify

load_dotenv()

# client = AzureOpenAI(
#     azure_endpoint=os.getenv("AZURE_APIM_ENDPOINT"),
#     api_key=os.getenv("AZURE_APIM_API_KEY"),
#     api_version="2023-12-01-preview",
# )

openai_api_key = os.getenv('OPENAI_API_KEY')

# Set the OpenAI API key
client = OpenAI(api_key=openai_api_key)

def get_code_from_github(repo, path, branch='master'):
    url = f"https://api.github.com/repos/{repo}/contents/{path}?ref={branch}"
    response = requests.get(url)
    if response.status_code == 200:
        file_info = response.json()
        if file_info['encoding'] == 'base64':
            return base64.b64decode(file_info['content']).decode()
        else:
            return "File encoding not supported."
    else:
        return "Error: " + response.content.decode()


def analyze_code(prompt, code, token_count):
    messages = [
        {"role": "system", "content": "You are CodeUnderstander, an AI model that understands code and describes it. Describe any code given to you in terms of what the code is for"},
        {"role": "user", "content": f"{prompt}\n\n{code}"},
    ]
    response = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=messages,
        max_tokens=token_count
    )
    # Adjusted access to the response content
    return response.choices[0].message.content.strip()


def convert_to_pseudocode(code, token_count):
    messages = [
        {"role": "system", "content": "You are AppilcationToPseudocodeGPT. Your job is to take in a Pseudocode definition template and fill the template to correspond to a given application. Do not lose any information, the pseudocode needs to represent the application in its entirety. Include the logic behind all functions as well as every component that will need to be created with styling. You will be provided 2 things, an application definition, the code, and you will use the following template as the basis."},
        {"role": "user", "content": f"Convert the following code to pseudocode:\n\n{code}"},
    ]
    response = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=messages,
        max_tokens=token_count
    )
    return response.choices[0].message.content.strip()

def update_json(json_data, modern_language, modern_stack):
    json_data['modern_language'] = modern_language
    json_data['modern_stack'] = modern_stack
    return json_data

def generate_modern_code(pseudocode, modern_language, modern_stack, token_count):
    prompt = f"Generate {modern_language} code using {modern_stack} for the following pseudocode:\n\n{pseudocode}. \n\n It's okay to add multiple files to your response as long as you clearly separate them."
    messages = [
        {"role": "system", "content": "You are PseudoStackGPT, you take the provided LLM parsable pseudocode and use it to build and code all the data specified in the pseudocode, in whatever languages and frameworks are specified, following the instructions exactly."},
        {"role": "user", "content": prompt},
    ]
    response = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=messages,
        max_tokens=token_count
    )
    return response.choices[0].message.content.strip()


def main(legacy_code, modern_language, modern_stack):
    # Analyze legacy code
    prompt = "Explain the following code in detail:"
    token_count = 1000  # adjust this value as needed
    analysis = analyze_code(prompt, legacy_code, token_count)
    with open('analysis.md', 'w', encoding='utf-8') as f:
        f.write("# Code Analysis\n\n" + analysis.replace("\n", "\n\n"))

    # Convert to pseudocode
    token_count = 1500  # adjust this value as needed
    pseudocode = convert_to_pseudocode(legacy_code, token_count)
    with open('pseudocode.md', 'w', encoding='utf-8') as f:
        f.write("# Pseudocode\n\n" + pseudocode.replace("\n", "\n\n"))

    # Update JSON
    json_data = {"modern_language": None, "modern_stack": None}
    updated_json = update_json(json_data, modern_language, modern_stack)
    with open('updated_json.json', 'w', encoding='utf-8') as f:
        json.dump(updated_json, f)

    # Generate modern code
    token_count = 2500  # adjust this value as needed
    modern_code = generate_modern_code(pseudocode, modern_language, modern_stack, token_count)
    with open('modern_code.py', 'w', encoding='utf-8') as f:
        f.write("Modern Code:\n" + modern_code)
        
# Usage
if __name__ == "__main__":
    repo = 'timophy/AlphabetSlots'  # GitHub repository
    path = 'slot.php'  # Path to the file in the repository
    branch = 'master'  # Branch name
    legacy_code = get_code_from_github(repo, path, branch)
    modern_language = "Python"
    modern_stack = "Flask"
    main(legacy_code, modern_language, modern_stack)