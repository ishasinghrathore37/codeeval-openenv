from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/reset")
def reset():
    return {"status": "reset"}

@app.post("/step")
def step(data: dict):
    return {"response": "ok", "reward": 1.0}

@app.get("/state")
def state():
    return {"status": "running"}


def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
