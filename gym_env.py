import gymnasium as gym
from gymnasium import spaces
from env.env import CodeEnv
from env.models import Action
from agent.llm_agent import LLMAgent

class RLWrapper(gym.Env):
    def __init__(self):
        super().__init__()
        self.env = CodeEnv()
        self.agent = LLMAgent()

        
        self.observation_space = spaces.Text(max_length=500)

        
        self.action_space = spaces.Discrete(1)

    def reset(self, seed=None, options=None):
        state = self.env.reset()

       
        return str(state.problem), {}

    def step(self, action):
        state_text = str(self.env.current_task["description"])

        
        code = self.agent.act(type("obj", (), {"problem": state_text}))

        result = self.env.step(Action(code=code))

        reward = float(result.reward)

        
        return (
            state_text,   
            reward,       
            True,         
            False,        
            {}            
        )