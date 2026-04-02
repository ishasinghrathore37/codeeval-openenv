from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
from openai import OpenAI


app = FastAPI()

@app.get("/")
def home():
    with open("index.html","r",encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

# Reset endpoint
@app.post("/reset")
def reset():
    return {"state": "Environment reset successful"}

# Step endpoint
@app.post("/step")
def step(data: dict):
    prompt = data.get("action", "")

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return {
        "response": response.choices[0].message.content,
        "reward": 0.8
    }

#state endpoint
@app.get("/state")
def state():
    return {
        "status":"running",
        "message":"Environment is active"
    }