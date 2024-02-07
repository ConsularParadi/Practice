from typing import List

def permutations(myString: str, l: int ,r: int, perm_dict: dict):
    if l==r:
        return None
    else:
        perm_dict[myString] = 1
        myList = list(myString)
        for i in range(l, r+1):
            myList[i], myList[l] = myList[l], myList[i]
            nextString = ''.join(myList)
            if nextString not in perm_dict:
                perm_dict[nextString] = 1
            permutations(''.join(myList), l+1, r, perm_dict)
    return list(perm_dict.keys())
        
perm_dict = {}
print(permutations('ABC',0,len("ABC")-1, perm_dict) )
