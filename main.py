from fastapi import FastAPI
from env.env import CodeEnv
from env.models import Action
from agent.llm_agent import LLMAgent

app = FastAPI()

env = CodeEnv()
agent = LLMAgent()

@app.get("/task")
def get_task():
    state = env.reset()
    return {
        "problem": state.problem,
        "difficulty": state.difficulty
    }

@app.post("/run")
def run_code():
    state = env.current_task

    best_reward = 0
    best_code = ""

    for _ in range(3):
        code = agent.act(type("obj", (), {"problem": state["description"]}))
        result = env.step(Action(code=code))

        if result.reward > best_reward:
            best_reward = result.reward
            best_code = code

    return {
        "best_code": best_code,
        "reward": best_reward
    }