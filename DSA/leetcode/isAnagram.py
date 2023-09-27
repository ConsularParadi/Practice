from collections import Counter

s = "anagram"
t = "nagaram"

def isAnagram_dict(s: str, t:str) -> bool:
    if len(s) != len(t):
        return False
    d1, d2 = {}, {}
    for i in range(len(s)):
        d1[s[i]] = d1.get(s[i], 0) + 1
        d2[t[i]] = d2.get(t[i], 0) + 1
    if d1 == d2: return True
    else: return False

def isAnagram_set(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    else:
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
    return True

def isAnagram(self, s: str, t:str) -> bool:
    if Counter(s) == Counter(t): return True
    else: return False
