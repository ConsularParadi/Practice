from typing import List
import random 

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = []
    res = [0]*len(temperatures)
    for i,temp in enumerate(temperatures):
        if not stack:
            stack.append([temp,i])
        else:
            counter = 0
            while stack!=[] and temp > stack[-1][0]:
                print(stack, counter)
                elem_idx = stack.pop()[1]
                res[elem_idx] = i - elem_idx  
            stack.append([temp,i])
    return res

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
