def twoSum_brute(nums: list[int], target: int) -> list[int]:        
    for i in range(len(nums)):
        a = nums[i]
        for j in range(i+1, len(nums)):
            b = nums[j]
            if a + b == target:
                return [i,j]
            
def twoSum_dict(nums: list[int], target: int) -> list[int]:
    d1 = {}
    for i, num in enumerate(nums):
        if (target - num) in d1:
            return [d1[target - num], i]
        else:
            d1[num] = i