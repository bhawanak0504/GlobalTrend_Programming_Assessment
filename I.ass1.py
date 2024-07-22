class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def delete(self, val):
        try:
            index = self.heap.index(val)
           
            self.heap[index] = self.heap[-1]
            self.heap.pop()
            self._heapify_down(index)
        except ValueError:
            print(f"Value {val} not found in heap.")
    
    def get_max(self):
        return self.heap[0] if self.heap else None
    
    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)
    
    def _heapify_down(self, index):
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)
    
    def __str__(self):
        return str(self.heap)


max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(5)
print("Heap after inserts:", max_heap)  

max_val = max_heap.get_max()
print("Max value:", max_val)  

max_heap.delete(20)
print("Heap after deleting max:", max_heap)  