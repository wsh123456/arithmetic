"""
    python中数组不会限制类型，在比如java中会限制，可以使用泛型
    Array<E>
"""


class Array():

    __data = []
    __size = 0

    # 默认数组容量为10的构造函数
    def __init__(self, capacity = 10):
        self.__data = [None]*capacity

    # 获取数组中的元素个数
    def getSize(self):
        return self.__size

    # 获取数组的容量
    def getCapacity(self):
        return len(self.__data)

    # 获取数组是否为空
    def isEmpty(self):
        return self.__size == 0

    # 向数组的第一个位置添加元素
    def addFirst(self, e):
        self.add(0, e)

    # 向所有元素末尾添加元素
    def addLast(self, e):
        self.add(self.__size, e)
        # if self.__size == len(self.__data):
        #     raise Exception("AddLast failed, Array is full.")
        # self.__data[self.__size] = e
        # self.__size += 1

    # 向第index的位置插入元素e
    def add(self, index, e):
        if index < 0 or index > self.__size:
            raise Exception("Add failed, Require index >= 0 and index <= size.")
        if self.__size == len(self.__data) - 1:
            self.__resize(2 * len(self.__data))
        i = self.__size
        while(index <= i):
            self.__data[i+1] = self.__data[i]
            i -= 1
        self.__data[i + 1] = e
        self.__size += 1

    # 获取data数组内index位置的元素e
    def get(self, index):
        if index < 0 or index >= self.__size:
            raise Exception("Get failed, index is illegal.")
        return self.__data[index]

    # 设置改变数组中某一个位置的值
    def set(self, index, e):
        if index < 0 or index >= self.__size:
            raise Exception("Set failed, index is illegal.")
        self.__data[index] = e

    # 用print输出时将数组转化为字符串
    def __str__(self):
        result = "Array : size is {0}, capacity is {1} .\n".format(self.__size, len(self.__data))
        result = result + "["
        for i in range(self.__size):
            result = result + str(self.__data[i])
            if i < self.__size - 1:
                result = result + ","
        result = result + "]"
        return result

    # 判断数组中是否含有某个元素e
    def contains(self, e):
        if e in self.__data:
            return True
        else:
            return False

    # 查找数组中某个元素的索引，若不存在返回-1
    def find(self, e):
        for i in range(self.__size):
            if e == self.__data[i]:
                return i
        return -1

    # 删除索引index位置的元素
    def remove(self, index):
        if index < 0 or index >= self.__size:
            raise Exception("Remove faild, index is illegal.")
        for i in range(index, self.__size):
            self.__data[i] = self.__data[i+1]
        self.__size -= 1
        if self.__size <= len(self.__data) // 3 and len(self.__data) != 0:
            self.__resize(len(self.__data) // 2)

    # 删除第一个元素
    def removeFirst(self):
        self.remove(0)

    # 删除最后一个元素
    def removeLast(self):
        self.remove(self.__size - 1)

    # 数组容量扩展为newSize
    def __resize(self, newSize):
        newdata = [None]*newSize
        for i in range(self.__size):
            newdata[i] = self.__data[i]
        self.__data = newdata




# if __name__ == "__main__":
#     a = Array(50)
#     for i in range(20):
#         a.addLast(i)
#     print(a)
#
#     # a.addFirst("first")
#     # print(a)
#     #
#     # a.add(10, "second")
#     # print(a)
#
#     # a.set(7, "set")
#     # print(a)
#     # print(a.get(7))
#
#     a.removeLast()
#     print(a)