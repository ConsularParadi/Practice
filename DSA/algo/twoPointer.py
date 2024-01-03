from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        num_sum = numbers[left] + numbers[right]
        if (num_sum == target):
            return [left+1, right+1]
        elif (num_sum < target):
            left += 1
        else:
            right -= 1
    return

print(twoSum([2,7,11,15], 9))