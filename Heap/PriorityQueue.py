# 优先队列
from arithmetic.MyQueue import Queue
from arithmetic.Heap.MaxHeap import MaxHeap

class PriorityQueue(Queue):
    def __init__(self):
        self.maxHeap = MaxHeap()

    def isEmpty(self):
        return self.maxHeap.isEmpty()

    def getSize(self):
        return self.maxHeap.getSize()

    def getFront(self):
        return self.maxHeap.findMax()

    def enqueue(self, e):
        self.maxHeap.add(e)

    def dequeue(self):
        return self.maxHeap.extractMax()