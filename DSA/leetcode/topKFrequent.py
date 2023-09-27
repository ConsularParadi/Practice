def topKFrequent_dict(self, nums: list[int], k: int) -> List[int]:
    count = [[num,count] for num, count in Counter(nums).items()]
    return sorted([val[0] for val in sorted(count, key=lambda e: (e[1], e[0]), reverse=True)[:k]])
