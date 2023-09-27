import numpy as np

def productExceptSelf_numpy(nums: list[int]) -> list[int]:
    np_nums = np.array(nums)
    res = [1] * len(nums)
    for i in range(len(nums)):
        temp = np_nums[i]
        np_nums[i] = 1
        res[i] = np.prod(np_nums)
        np_nums[i] = temp
    return res

def productExceptSelf_prefixPostfix(nums: list[int]) -> list[int]:
    res = [1] * len(nums)
    l, r = 1, 1
    for i in range(len(nums)):
        res[i] = l
        l *= nums[i]
    for i in range(-1, -int(len(nums)+1), -1):
        res[i] *= r
        r *= nums[i]
    return res