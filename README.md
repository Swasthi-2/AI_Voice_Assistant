AI_Voice_Assistant(FastAPI)
A simple AI-powered voice assistant API built using FastAPI, with intent recognition and MongoDB for conversation storage.

Project Description
This project is an AI voice assistant that uses the FastAPI to process text input (simulate voice) and respond appropriately. The assistant determines the user's purpose using Natural Language Processing (NLP) and reacts appropriately.

Features
* RESTful API based on FastAPI.
* Intent recognition (unknown inquiries, goodbyes, and greets).
* OpenAI GPT-3.5 integration is optional for intelligent responses.
* MongoDB is supported for storing chat exchanges. Docker containerization makes deployment simple.
* The OpenAPI documentation can be found at /docs.

Setup Instructions

1.Clone the Repository
git clone https://github.com/Swasthi-2/Ai_Voice_Assistant.git
cd AI_Voice-Assistant

2.Set Up a Virtual Environment
python -m venv venv
venv/Scripts/activate

3.Install Dependencies
uvicorn main:app --reload
API will be available at: http://127.0.0.1:8000/docs

API Usage Examples
1. Process Text Input
Endpoint: POST /process

Request Body (JSON):
{
  "text": "Hi"
}

Response Example:
{
  "user_input": "hi",
  "response": "Hello! How can I help you?"
}

Docker Instructions

1.Build Docker Image
docker build -t ai_voice .

2.Run Docker Container
docker run -p 8000:8000 ai_voice
Visit API Docs: http://localhost:8000/docs

3.Push to Docker Hub
docker tag ai_voice swasthi2/ai_voice
docker push swasthi2/ai_voice

Push to GitHub
git add .
git commit -m "First commit"
git branch -M main
git remote add origin https://github.com/Swasthi-2/Ai_Voice_Assistant.git
git push -u origin main










