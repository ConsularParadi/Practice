from typing import List

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    stack = []
    carFleet = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
    for car in carFleet:
        time_taken = (target - car[0])/car[1]
        if len(stack) >= 1:
            if time_taken <= stack[-1]:
                continue
        stack.append(time_taken)
    return len(stack)

#res = carFleet(10, [0,4,2], [2,1,3])
res = carFleet(12, [10,8,0,5,3],[2,4,1,1,3])
print(res)
