from fastapi import FastAPI, HTTPException
from gemini_api import debug_code

app = FastAPI()

@app.post("/debug/")
def analyze_code(code: dict):
    """
    API endpoint to receive a code snippet and return debugging suggestions.
    """
    if "code" not in code:
        raise HTTPException(status_code = 400, detail = "Code snippet not found in request.")
    
    response = debug_code(code["code"]) 
    return {"debug_suggestions": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port = 8000)
 
