from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import os
from openai import OpenAI

app = FastAPI()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.get("/", response_class=HTMLResponse)
def home():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "<h1>UI not found</h1>"

@app.post("/reset")
def reset():
    return {"status": "reset"}

@app.post("/step")
def step(data: dict):
    try:
        user_input = data.get("input", "Hello")

        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        output = response.choices[0].message.content

        return {
            "response": output,
            "reward": 1.0
        }

    except Exception as e:
        
        return {
            "response": "error handled",
            "reward": 0.0,
            "error": str(e)
        }

@app.get("/state")
def state():
    return {"status": "running"}


# ✅ Run server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
