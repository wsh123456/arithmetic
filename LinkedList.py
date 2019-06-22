class LinkedList():

    class __Node():
        def __init__(self, e = None, next = None):
            self.e = e
            self.next = next

        def __str__(self):
            return str(self.e)

    def __init__(self):
        # 为链表设置一个虚拟头节点，以便在链表头插入操作
        self.__dummyHead = self.__Node()
        self.__size = 0

    # 获取链表中的元素个数
    def getSize(self):
        return self.__size

    # 获取链表是否为空
    def isEmpty(self):
        return self.__size == 0

    # 在index的位置添加元素e
    def add(self, index, e):
        # 先检验index的合法性
        # 如果在head的位置插入，则addFirst
        # 不是head的话则新一个node，找到index-1的位置，指向他的next再将index-1的next指向node
        # 维护size
        if index < 0 or index > self.__size:
            raise Exception("Add failed, Require index >= 0 and index <= size.")

        prev = self.__dummyHead
        for i in range(index):
            prev = prev.next

        # node = self.__Node(e)
        # node.next = prev.next
        # prev.next = node
        prev.next = self.__Node(e, prev.next)
        self.__size += 1

    # 在链表的头添加新的元素e
    def addFirst(self, e):
        self.add(0, e)

    # 在链表末尾位置添加元素e
    def addLast(self, e):
        self.add(self.__size, e)

    # 获取链表第index个位置的元素
    def get(self, index):
        if index < 0 or index >= self.__size:
            raise Exception("Get failed, Illegal index.")
        current = self.__dummyHead.next
        for i in range(index):
            current = current.next
        return current.e

    def getFirst(self):
        return self.get(0)

    def getLast(self):
        return self.get(self.__size - 1)

    # 修改链表中第index位置的元素
    def set(self, index, e):
        if index < 0 or index >= self.__size:
            raise Exception("Set failed, Illegal index.")
        current = self.__dummyHead.next
        for i in range(index):
            current = current.next
        current.e = e

    # 查找链表中是否存在元素e
    def contains(self, e):
        current = self.__dummyHead.next
        while current:
            if current.e == e:
                return True
            current = current.next
        return False

    # 从链表中删除第index个元素，并返回被删除的元素
    def remove(self, index):
        if index < 0 or index >= self.__size:
            raise Exception("Remove failed, Illegal index.")
        previous = self.__dummyHead
        for i in range(index):
            previous = previous.next
        retNode = previous.next
        previous.next = retNode.next
        retNode.next = None
        self.__size -= 1

        return retNode.e

    def removeFirst(self):
        return self.remove(0)

    def removeLast(self):
        return self.remove(self.__size - 1)

    def __str__(self):
        current = self.__dummyHead.next
        result = "LinkedList : "
        while current != None:
            result += str(current) + " -> "
            current = current.next
        result += "None"
        return result


# if __name__ == "__main__":
#     linkedList = LinkedList()
#     for i in range(5):
#         linkedList.addFirst(i)
#         print(linkedList)
#     linkedList.add(2, 666)
#     print(linkedList)
#
#     linkedList.remove(2)
#     print(linkedList)
#     linkedList.removeFirst()
#     print(linkedList)
#     linkedList.removeLast()
#     print(linkedList)