from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
from get_llm_response import get_answer

app = FastAPI()

# CORS settings
origins = ["*"]  # Allow all origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Input Request Model
class QuestionRequest(BaseModel):
    provider: str
    model: str
    question: str

# Output Response Model
class AnswerResponse(BaseModel):
    answer: str

# Post endpoint to handle question requests
@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    # Placeholder logic for generating an answer
    # In a real application, you would integrate with an AI model or database here
    answer = f"{get_answer(request.question, request.provider, request.model)}"
    
    return {"answer": answer}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)