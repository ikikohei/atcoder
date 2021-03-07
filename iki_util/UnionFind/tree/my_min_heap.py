import math

INFTY = 2**31 -1

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

class MyHeap:
    def __init__(self, arr):
        self.arr = arr
        self.size = 0
        self.create_min_heap()
    
    def min_heapify(self, index):
        left = self.get_left(index)
        right = self.get_right(index)
        if left < self.size and self.arr[left] < self.arr[index]:
            smallest = left
        else:
            smallest = index
        if right < self.size and self.arr[right] < self.arr[smallest]:
            smallest = right

        if smallest != index:
            swap(self.arr, index, smallest)
            self.min_heapify(smallest)
    
    def create_min_heap(self):
        self.size = len(self.arr)
        for i in range(math.floor(self.size / 2) -1, -1, -1):
            self.min_heapify(i)
        
    def get_parent(self, index):
        return math.floor((index + 1) / 2) - 1
    
    def get_left(self, index):
        return 2 * (index + 1) - 1
    
    def get_right(self, index):
        return 2 * (index + 1)

    def extract_min(self):
        if self.size < 1:
            print("heap is empty")
            return None
        
        min = self.arr[0]
        self.arr[0] = self.arr[self.size - 1 ]
        self.arr.pop(self.size - 1)
        self.size -= 1
        self.min_heapify(0)

        return min

    def insert(self, val):
        self.size += 1
        self.arr.append(INFTY)
        self.decrease_val(self.size-1, val)
    
    def decrease_val(self, index, val):
        if self.arr[index] < val:
            print("val is not decreased")
            return None
        
        self.arr[index] = val
        while index > 0 and self.arr[self.get_parent(index)] > self.arr[index]:
            swap(self.arr, index, self.get_parent(index))
            index = self.get_parent(index)
        
    def heap_sort(self):
        for i in range(self.size - 1, 0, -1):
            swap(self.arr, 0, i)
            self.size -= 1
            self.min_heapify(0)
        
        self.size = len(self.arr)
    
    def to_string(self):
        return str(self.arr[:self.size])
    
if __name__=='__main__':
    arr = [6,3,18,1,13]
    my_heap = MyHeap(arr)
    print("the heap after max heapify: ", my_heap.to_string())