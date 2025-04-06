from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gemini_api import get_debugging_response

# Initialize FastAPI app
app = FastAPI(title = "Fixora AI Debugger",
              description = "An API that provides AI-driven debugging assistance for programming errors.",
              version = "1.0")

# Define request model
class CodeRequest(BaseModel):
    code: str

@app.post("/debug/")
def debug_code(request: CodeRequest):
    """
    Endpoint to analyze and debug provided code.
    """
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Code snippet cannot be empty.")
    
    response = get_debugging_response(request.code)
    return {"debugging_details": response}
