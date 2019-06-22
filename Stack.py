from arithmetic.Array import Array


class Stack():
    def pop(self):pass
    def push(self, e):pass
    def peek(self):pass
    def isEmpty(self):pass
    def getSize(self):pass


class ArrayStack(Stack):

    array = Array()

    def __init__(self, capacity = 10):
        self.array = Array(capacity)

    def pop(self):
        return self.array.removeLast()

    def push(self, e):
        self.array.addLast(e)

    # 查看栈顶元素
    def peek(self):
        return self.array.get(self.getSize() - 1)

    def getSize(self):
        return self.array.getSize()

    def isEmpty(self):
        return self.array.isEmpty()

    def getCapacity(self):
        return self.array.getCapacity()

    def __str__(self):
        result = "Stack: "
        result += "["
        for i in range(self.getSize()):
            result += str(self.array.get(i))
            if i < self.getSize() - 1:
                result += ","
        result += "] top"
        return result

# arr = ArrayStack()
# for i in range(5):
#     arr.push(i)
#     print(arr)
# arr.pop()
# print(arr)