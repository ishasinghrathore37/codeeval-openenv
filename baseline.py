from env.env import CodeEnv
from env.models import Action
from agent.llm_agent import LLMAgent

env = CodeEnv()
agent = LLMAgent()

# reset env
state = env.reset()

print("\n📌 Problem:", state.problem)
print("Difficulty:", state.difficulty)

best_reward = 0
best_code = ""

# retry system
for i in range(3):
    print(f"\n--- Attempt {i+1} ---")

    # IMPORTANT: state.problem pass karna
    code = agent.act(state)

    # wrap in Action model
    action = Action(code=code)

    # env step
    result = env.step(action)

    print("Reward:", result.reward)

    if result.reward > best_reward:
        best_reward = result.reward
        best_code = code

print("\n🔥 BEST CODE:\n", best_code)
print("🏆 FINAL REWARD:", best_reward)