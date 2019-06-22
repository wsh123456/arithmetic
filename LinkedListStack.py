from arithmetic import Stack, LinkedList
import time

class LinkedListStack(Stack.Stack):
    def __init__(self):
        self.list = LinkedList.LinkedList()

    def getSize(self):
        return self.list.getSize()

    def isEmpty(self):
        return self.isEmpty()

    def push(self, e):
        self.list.addFirst(e)

    def pop(self):
        return self.list.removeFirst()

    def peek(self):
        return self.list.getFirst()

    def __str__(self):
        result = "Stack : top " + str(self.list)
        return result


if __name__ == "__main__":
#     linkedList = LinkedListStack()
#     for i in range(5):
#         linkedList.push(i)
#         print(linkedList)
#
#     linkedList.pop()
#     print(linkedList)

    def test(queue, opCount):
        startTime = int(time.time() * 1000)
        testStack = queue()
        for i in range(opCount):
            testStack.push(i)
        for i in range(opCount):
            testStack.pop()

        endTime = int(time.time() * 1000)
        return (endTime - startTime) / 1000

    opCount = 10000000
    time1 = test(Stack.ArrayStack, opCount)
    print("ArrayStack : ", time1, " s")
    time2 = test(LinkedListStack, opCount)
    print("LinkedListStack : ", time2, " s")
