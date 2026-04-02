import json
import random
import os
from env.models import State, Action, StepResult
from env.evaluator import evaluate_code
from env.rewards import compute_reward

class CodeEnv:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        TASK_PATH = os.path.join(BASE_DIR, "tasks", "tasks.json")

        with open(TASK_PATH) as f:
            self.tasks = json.load(f)

    def reset(self):
        self.current_task = random.choice(self.tasks)

        return State(
            problem=self.current_task["description"],
            difficulty=self.current_task["difficulty"]
        )

    def step(self, action: Action):
        score = evaluate_code(action.code, self.current_task)
        reward = compute_reward(score, action.code)

        return StepResult(
            reward=reward,
            done=True,
            info={"score": score}
        )