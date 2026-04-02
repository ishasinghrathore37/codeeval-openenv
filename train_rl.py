from stable_baselines3 import PPO
from env.gym_env import RLWrapper

env = RLWrapper()

model = PPO("MlpPolicy", env, verbose=1)

model.learn(total_timesteps=1000)

model.save("ppo_code_agent")