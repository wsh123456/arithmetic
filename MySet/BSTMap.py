# 映射
# 用来存储(键 值)数据对的数据结构
# 与dict十分相似

# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，
# 并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
#
# 例如，对于list [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# 如果希望把list的每个元素都作平方，就可以用map()函数：
# 因此，我们只需要传入函数f(x)=x*x，就可以利用map()函数完成这个计算：
#
# def f(x):
#     return x*x
# print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# 输出结果：
#
# [1, 4, 9, 10, 25, 36, 49, 64, 81]
# 注意：map()函数不改变原有的 list，而是返回一个新的 list。


# 自己的映射类myMap实现可使用链表，二分搜索树实现
# 将key和value存储在同一个节点中即可

from arithmetic.MySet.base import MapBase

class BSTMap(MapBase):
    class __Node():
        def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None
        self.size = 0

    def isEmpty(self): return self.size == 0

    def getSize(self): return self.size

    def add(self, key, value):
        self.root = self.__addR(self.root, key, value)

    # 向以node为根节点的二分搜索树的映射中添加key和value
    # 递归算法recursion
    def __addR(self, node, key, value):
        if not node:
            self.size += 1
            return self.__Node(key, value)
        if key == node.key:
            node.value = value
            return
        elif key < node.key:
            node.left = self.__addR(node.left, key, value)
        elif key > node.key:
            node.right = self.__addR(node.right, key, value)

        return node

    # 返回以node为根节点的二分搜索树中key所在的节点
    def __getNode(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self.__getNode(node.left, key)
        else:
            return self.__getNode(node.right, key)

    def contains(self, key):
        return self.__getNode(self.root, key) is not None

    def get(self, key):
        node = self.__getNode(self.root, key)
        return node.value if node else None

    def set(self, key, value):
        node = self.__getNode(self.root, key)
        if not node:
            raise Exception(key + " doesnot exist")
        else:
            node.value = value

    # 找到以node为根节点的最小值节点
    def __minimum(self, node):
        if not node.left:
            return node
        return self.__minimum(node.left)

    # 删除以node为根的二分搜索树中的最小节点
    # 返回删除节点后的新二分搜索树的根
    def __removeMin(self, node):
        if not node.left:
            rightNode = node.right
            node.right = None
            self.size -= 1
            return rightNode
        node.left = self.__removeMin(node.left)
        return node

    def remove(self, key):
        self.root = self.__removeR(self.root, key)

    # 删除掉以node为根节点的二分搜索树中键为key的节点
    # 返回删除节点后新的二分搜索树的根,递归recursion
    def __removeR(self, node, key):
        if not node:
            return None

        if key < node.key:
            node.left = self.__removeR(node.left, key)
            return node
        elif key > node.key:
            node.right = self.__removeR(node.right, key)
            return node
        else:
            if not node.left:
                rightNode = node.right
                node.right = None
                self.size -= 1
                return rightNode
            elif not node.right:
                leftNode = node.left
                node.left = None
                self.size -= 1
                return leftNode
            successor = self.__minimum(node.right)
            successor.right = self.__removeMin(node.right)
            successor.left = node.left

            node.left = node.right = None
            return successor


if __name__ == '__main__':
    words = ''
    with open('shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    from time import time

    start_time = time()
    bst_map = BSTMap()
    for word in words:
        if bst_map.contains(word):
            bst_map.set(word, bst_map.get(word) + 1)
        else:
            bst_map.add(word, 1)

    print('Total words: ', len(words))
    print('Unique words: ', bst_map.getSize())
    print('Contains word "they": ', bst_map.contains('they'))
    ## 耗时1.23秒左右
    print('Total time: {} seconds'.format(time() - start_time))

    bst_map.remove('they')
    print(bst_map.contains('they'))
    # bst_map.set('they', 100)
    # print(bst_map.get('they'))