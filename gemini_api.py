import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def is_debugging_query(prompt: str) -> bool:
    """
    Checks if the prompt is related to code debugging.
    """
    keywords = ["fix", "error", "debug", "exception", "traceback", "issue"]
    return any(keyword in prompt.lower() for keyword in keywords)

def get_debugging_response(code_snippet: str) -> str:
    """
    Sends a code snippet to the Gemini API and retrieves a structured debugging response.
    """
    if not is_debugging_query(code_snippet):
        return "I only assist with code debugging. Please provide a code snippet with errors."

    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(
            f"Analyze and debug the following code:\n\n{code_snippet}\n\n"
            "Provide a structured breakdown including:\n"
            "1. Identified Errors\n"
            "2. Suggested Fixes\n"
            "3. Potential Optimizations\n"
        )
        return response.text
    except Exception as e:
        return f"An error occurred while processing your request: {str(e)}"
    
if __name__ == "__main__":
    
    # Testing the function with a sample code snippet
    code_snippet = """
    def divide(a, b):
        return a / b

    print(divide(10, 0))
    Check for errors
    """
    response = get_debugging_response(code_snippet)
    print(response) 