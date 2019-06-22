from arithmetic.MySet.base import MapBase

class LinkedListMap(MapBase):
    class __Node():
        def __init__(self, key=None, value=None, next=None):
            self.key = key
            self.value = value
            self.next = next

        def __str__(self):
            return self.key + ": " + self.value


    def __init__(self):
        self.dummyhead = self.__Node()
        self.size = 0

    def isEmpty(self): return self.size == 0

    def getSize(self): return self.size

    # 一个辅助函数，输入key的时候返回对应的节点
    def __getNode(self, key):
        current = self.dummyhead.next
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    # 查看key对应的节点是否存在
    def contains(self, key):
        return self.__getNode(key) is not None

    # 获取key对应的value值
    def get(self, key):
        resultNode = self.__getNode(key)
        return resultNode.value if resultNode else None

    # 向映射中添加元素(映射中的key唯一，当重复传入时覆盖更新)
    def add(self, key, value):
        node = self.__getNode(key)
        if not node:
            self.dummyhead.next = self.__Node(key, value, self.dummyhead.next)
            self.size += 1
        else:
            node.value = value

    # 更新一个key的value值
    def set(self, key, value):
        node = self.__getNode(key)
        if not node:
            raise Exception(key + " doesnot exist")
        node.value = value

    # 删除映射中key的节点
    def remove(self, key):
        previous = self.dummyhead
        while previous.next:
            if previous.next.key == key:
                break
            previous = previous.next

        if previous.next:
            delnode = previous.next
            previous.next = delnode.next
            delnode.next = None
            self.size -= 1
            return delnode.value
        return None


if __name__ == '__main__':
    words = ''
    with open('shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    from time import time

    start_time = time()
    linkedlist_map = LinkedListMap()
    for word in words:
        if linkedlist_map.contains(word):
            linkedlist_map.set(word, linkedlist_map.get(word) + 1)
        else:
            linkedlist_map.add(word, 1)

    print('Total words: ', len(words))
    print('Unique words: ', linkedlist_map.getSize())
    print('Contains word "they": ', linkedlist_map.contains('they'))
    # 耗时290秒左右
    print('Total time: {} seconds'.format(time() - start_time))