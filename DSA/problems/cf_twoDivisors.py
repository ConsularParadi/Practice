from typing import List

def two_divisors(nums: List[int]):
    if 1 in nums:
        return max(nums)**2
    num1 = max(nums)
    num2 = min(nums)
    test = num1*2
    while test <= num1*num2:
        greaterFactor = False
        if test % num2 == 0:
            test_num = num2*2
            while test_num < num1:
                if test%test_num == 0:
                    greaterFactor = True
                    break
                test_num += num2
            if not greaterFactor:
                return test
        test += num1
    return test

tC = int(input())
res = []
for _ in range(tC):
    myInput = input()
    a,b = list(map(int, myInput.split()))
    res.append(two_divisors([a,b]))
    tC -= 1
[print(result) for result in res]

# tC = 8
# tCases = [[2,3],[1,2],[3,11],[1,5],[5,10],[4,6],[3,9],[250000000,500000000]]
# while tC > 0:
#     a,b = tCases[tC-1]
#     print(a,b)
#     print(two_divisors([a,b]))
#     tC -= 1

print(two_divisors([11,33]))

"""
8
2 3
1 2
3 11
1 5
5 10
4 6
3 9
250000000 500000000
"""
