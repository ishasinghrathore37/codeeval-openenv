from transformers import pipeline

class LLMAgent:
    def __init__(self):
        self.generator = pipeline(
            "text-generation",
            model="sshleifer/tiny-gpt2",
            max_new_tokens=100
        )

    def act(self, state):
        prompt = f"""
Write a Python function named 'solution' for the problem:

{state.problem}

Only return code.
"""

        output = self.generator(prompt)[0]["generated_text"]

        return output