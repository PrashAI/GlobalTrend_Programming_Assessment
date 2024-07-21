
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
            if index < len(self.heap):
                self._heapify_down(index)
                self._heapify_up(index)
        except ValueError:
            print("Value not found in heap")

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

# Example usage:
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(15)
max_heap.insert(20)
max_heap.insert(17)

print("Max value:", max_heap.get_max())  # Should print 20

max_heap.delete(15)
print("Max value after deleting 15:", max_heap.get_max())  # Should print 20

max_heap.delete(20)
print("Max value after deleting 20:", max_heap.get_max())  # Should print 17
