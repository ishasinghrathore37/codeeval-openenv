def compute_reward(score, code):
    reward = score

    
    penalty = min(len(code) / 800, 0.2)

    
    bonus = 0.1 if score == 1.0 else 0

    reward = reward - penalty + bonus

    return max(0.0, min(1.0, reward))