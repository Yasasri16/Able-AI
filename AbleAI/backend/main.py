import sys
import os

# Add the parent directory (AbleAI/AbleAI) to Python's path so it can find 'llm'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()

from fastapi import FastAPI
from llm.response_generator import generate_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
class GestureInput(BaseModel):
    sentence: str

@app.get("/")
def read_root():
    return {"message": "AbleAI Backend is running successfully!"}
latest_gesture_output = {"sentence": ""}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (hackathon-safe)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process-gesture")
def process_gesture(data: GestureInput):
    result = generate_response(data.sentence)

    return {
        "corrected_input": result["corrected_input"],
        "response": result["response"]
    }
