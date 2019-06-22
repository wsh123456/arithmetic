from arithmetic import MyQueue


class LinkedListQueue(MyQueue.Queue):
    class __Node():
        def __init__(self, e = None, next = None):
            self.e = e
            self.next = next

        def __str__(self):
            return str(self.e)

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def getSize(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def enqueue(self, e):
        if self.__tail is None:
            self.__tail = self.__Node(e)
            self.__head = self.__tail
        else:
            self.__tail.next = self.__Node(e)
            self.__tail = self.__tail.next
        self.__size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Cannot dequeue from an empty queue.")
        result = self.__head
        self.__head = self.__head.next
        result.next = None
        if self.__head is None:
            self.__tail = None
        self.__size -= 1
        return result.e

    def getFront(self):
        if self.isEmpty():
            raise Exception("Queue is empty.")
        return self.__head.e

    def __str__(self):
        current = self.__head
        result = "LinkedListQueue : front "
        while current is not None:
            result += str(current) + " -> "
            current = current.next
        result += "None tail"
        return result


if __name__ == "__main__":
    aq = LinkedListQueue()
    for i in range(10):
        aq.enqueue(i)
        print(aq)
        if i % 3 == 2:
            aq.dequeue()
            print(aq)