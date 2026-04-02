class BaselineAgent:
    def act(self, state):
        
        if "two numbers" in state.problem:
            return """
def solution(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
"""
        return """
def solution(x):
    return True
"""