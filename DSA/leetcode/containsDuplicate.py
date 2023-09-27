def containsDuplicate(nums: list[int]) -> bool:
    dup_arr =  {}
    for num in nums:
        if num in dup_arr:
            return True
        else:
            dup_arr.append(num)
    return False