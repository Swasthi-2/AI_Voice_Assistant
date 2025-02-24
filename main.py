from fastapi import FastAPI
from pydantic import BaseModel
import openai  

app = FastAPI()

class UserInput(BaseModel):
    text: str

@app.post("/process")
async def process_text(input_data: UserInput):
    user_text = input_data.text.lower()

    # Basic Intent Matching
    if "hi" in user_text:
        response = "Hello! How can I help you?"
    elif "bye" in user_text:
        response = "Goodbye! Have a great day!"
    else:
        response = "I'm not sure how to respond."

    return {"user_input": user_text, "response": response}
