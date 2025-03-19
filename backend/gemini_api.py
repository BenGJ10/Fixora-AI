import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="config/.env")

# Ensure API key is set correctly
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ ERROR: GEMINI_API_KEY is missing. Please set it in the .env file.")

# Initialize Gemini API with the key
genai.configure(api_key=API_KEY)

def debug_code(code_snippet):
    """
    Function to send a code snippet to Gemini API and get debugging suggestions.
    """
    prompt = f"Analyze this code and provide a structured debugging report with clear sections: \n\
    1. **Critical Errors** (Syntax, missing imports, undefined variables) \n\
    2. **Code Optimization** (Unnecessary variables, redundant code, performance improvements) \n\
    3. **Best Practices** (Docstrings, naming conventions, formatting) \n\n\
    Provide suggestions in a well-structured format with proper markdown styling."
    
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  
        response = model.generate_content(prompt + "\n\n" + code_snippet)
        
        # Enhanced professional output formatting
        structured_output = f"\n🚀 **Debugging Report:**\n\n{response.text}\n"
        return structured_output  
    
    except Exception as e:
        return f"Error: {str(e)}"
