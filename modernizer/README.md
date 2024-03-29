# Modernizer

The Modernizer is a Python script that uses OpenAI's GPT-4 to analyze, convert to pseudocode, and generate modern code from legacy code.

## Usage

To use the Modernizer, you need to provide the GitHub repository, path to the file in the repository, and the branch name. The script will fetch the code, analyze it, convert it to pseudocode, and generate modern code in Python using Flask.

```sh
python app.py
```

## Functions

- get_code_from_github(repo, path, branch='master'): 
    - **Fetches the code from the specified GitHub repository.**
- analyze_code(prompt, code, token_count): 
    - **Analyzes the fetched code.**
- convert_to_pseudocode(code, token_count): 
    - **Converts the analyzed code to pseudocode.**
- update_json(json_data, modern_language, modern_stack): 
    - **Updates a JSON file with the modern language and stack.**
- generate_modern_code(pseudocode, modern_language, modern_stack, token_count): 
    - **Generates modern code from the pseudocode.**

## Files

- *app.py*:
    - The main script.
- *analysis.md*:
    - Contains the analysis of the legacy code.
- *pseudocode.md*:
    - Contains the pseudocode generated from the legacy code.
- *updated_json.json*:
    - Contains the updated JSON data.
- *modern_code.py*: 
    - Contains the generated modern code.