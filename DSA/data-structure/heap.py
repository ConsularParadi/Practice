from typing import List

class PriorityPair():
    def __init__(self, pair: tuple):
        self.value = pair[0]
        self.priority = pair[1]
        self.pair = pair

    def __lt__(self, other):
        return self.pair[1] < other.pair[1]
    
    def __gt__(self, other):
        return self.pair[1] > other.pair[1]
    
    def __eq__(self, other):
        return self.pair[1] == other.pair[1]

    def __str__(self):
        return str(self.pair)

class MaxHeap():
    
    def __init__(self, arr: dict):
        self.arr = [PriorityPair(elem) for elem in arr.items()]
        self.heapSize = len(arr)
        self.heapify()

    def get_children(self, parent_idx: int):
        if(2*parent_idx+2 <= self.heapSize - 1):
            return [[self.arr[(2*parent_idx)+1], (2*parent_idx)+1], [self.arr[(2*parent_idx)+2], (2*parent_idx)+2]]
        elif(2*parent_idx+2 > self.heapSize - 1 and 2*parent_idx+1 <= self.heapSize - 1):
            return [[self.arr[(2*parent_idx)+1], (2*parent_idx)+1]]

    def swap(self, i: int, j:int):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def insert(self, value):
        self.arr.append(value)
        self.heapSize += 1
        idx = self.heapSize - 1
        while (idx >= 1 and self.arr[idx] > self.arr[(idx-1)//2]):
            self.swap(idx, (idx-1)//2)
            idx = (idx-1)//2

    def delete(self):
        self.swap(0, self.heapSize - 1)
        self.heapSize -= 1
        idx = 0
        while (idx <= ((self.heapSize//2)-1) and self.arr[idx] < self.arr[max(self.get_children(idx), key=lambda x: x[0].priority)[1]]):
            max_idx = max(self.get_children(idx), key=lambda x: x[0].priority)[1]
            self.swap(idx, max_idx)
            idx = max_idx
    
    def heapify(self):
        idx = (self.heapSize - 1)//2
        while (idx >= 0):
            original_idx = idx
            print(2*idx + 1)
            if ((2*idx)+1) > self.heapSize - 1:
                idx -= 1
                continue
            while (self.arr[idx] < self.arr[max(self.get_children(idx), key=lambda x: x[0].priority)[1]]):
                max_idx = max(self.get_children(idx), key=lambda x: x[0].priority)[1]
                print(max_idx)
                print(self.arr[idx].value, self.arr[max_idx].value)
                self.swap(idx, max_idx)
                idx = min((self.heapSize)//2 - 1, max_idx)
            idx = original_idx - 1

    def __str__(self):
        idx = 0
        string = ""
        while idx < self.heapSize//2:
            string += f"Node: {self.arr[idx].value} -> Children: {[x[0].value for x in self.get_children(idx)]}\n"
            idx += 1
        return string
