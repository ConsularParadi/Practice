from collections import defaultdict

def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    d1 = defaultdict(list)
    for s in strs:
        d1["".join(sorted(s))].append(s)
    return d1.values()