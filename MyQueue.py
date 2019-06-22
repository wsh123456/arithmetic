# 实现循环队列来解决数组队列对于出队操作时间复杂度为O(n)
# 使用循环队列 用均摊分析发可以为O(1)




from arithmetic.Array import Array
import time


class Queue():
    def enqueue(self, e):pass
    def dequeue(self):pass
    def getFront(self):pass
    def getSize(self):pass
    def isEmpty(self):pass


# 数组队列的实现
class ArrayQueue(Queue):

    array = []

    def __init__(self, capacity = 10):
        self.array = Array(capacity)

    def enqueue(self, e):
        self.array.addLast(e)

    def dequeue(self):
        self.array.removeFirst()

    def getSize(self):
        return self.array.getSize()

    def getFront(self):
        return self.getFront()

    def isEmpty(self):
        return self.array.isEmpty()

    def getCapacity(self):
        return self.array.getCapacity()

    def __str__(self):
        result = "Queue: front ["
        for i in range(self.array.getSize()):
            result += str(self.array.get(i))
            if i < self.getSize() - 1:
                result += ","
        result += "] tail"
        return result


# 循环队列的实现
class LoopQueue(Queue):

    def __init__(self, capacity = 10):
        # 循环队列默认队尾与队首之间要有一个空位，
        # 否则当队首和队尾相同时表示队列为空
        self.__data = [None] * (capacity + 1)
        self.__front = 0
        self.__tail = 0
        self.__size = 0

    def getCapacity(self):
        return len(self.__data) - 1

    def isEmpty(self):
        return self.__front == self.__tail

    def getSize(self):
        return self.__size

    def enqueue(self, e):
        # 如果队列满了，resize
        if (self.__front - 1) % len(self.__data) == self.__tail:
            self.__reSize(2 * self.getCapacity())
        # 在tail的位置入队
        self.__data[self.__tail] = e
        self.__tail = (self.__tail + 1) % len(self.__data)
        self.__size += 1

    def dequeue(self):
        # 先判断队列是否为空，为空报错
        if self.isEmpty():
            raise Exception("Connot dequeue from an empty queue")
        # 不为空将队首元素移除，维护front和size
        result = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__front = (self.__front + 1) % len(self.__data)
        self.__size -= 1
        if self.__size <= self.getCapacity() // 4 and self.__size <= self.getCapacity() // 2 != 0:
            self.__reSize(self.getCapacity() // 2)
        return result

    def __reSize(self, length):
        newdata = [None] * length
        for i in range(self.__size):
            newdata[i] = self.__data[(self.__front + i) % len(self.__data)]
        self.__data = newdata
        self.__front = 0
        self.__tail = self.__size

    def getFront(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.__data[self.__front]

    def __str__(self):
        result = "Queue: front ["
        for i in range(self.getSize()):
            result += str(self.__data[(self.__front + i) % len(self.__data)])
            if (self.__front + i) % len(self.__data) != self.__tail -1:
                result += ","
        result += "] tail"
        return result


if __name__ == "__main__":
    pass
    # aq = LoopQueue()
    # for i in range(10):
    #     aq.enqueue(i)
    #     print(aq)
    #     if i % 3 == 2:
    #         aq.dequeue()
    #         print(aq)

    # 测试用例




