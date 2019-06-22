class MaxHeap():
    def __init__(self, arr = None):
        self.__heapList = []
        # heapify 将任意数组整理成堆的形状
        if arr:
            self.__heapList = arr
            i = self.__parent(len(self.__heapList) - 1)
            while i >= 0:
                self.__siftDown(i)
                i -= 1

    def getSize(self):
        return len(self.__heapList)

    def isEmpty(self):
        return self.__heapList.__len__() == 0

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的父亲节点的索引
    def __parent(self, index):
        if index == 0:
            raise Exception("index-0 doesn't have parent")
        return (index - 1) // 2

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的左孩子节点的索引
    def __leftchild(self, index):
        return index * 2 + 1

    # 返回完全二叉树的数组表示中，一个索引所表示的元素的右孩子节点的索引
    def __rightchild(self, index):
        return index * 2 + 2

    # 向堆中添加元素e，Sift up，上浮法
    # 1.先向堆尾部添加这个元素
    # 2.用添加后的元素(索引为堆的lenth-1)与其父亲节点比较，小则交换位置循环
    def add(self, e):
        self.__heapList.append(e)
        self.__siftUp(self.getSize() - 1)

    def __siftUp(self, index):
        while index > 0 and self.__heapList[index] > self.__heapList[self.__parent(index)]:
            # 交换位置
            self.__heapList[index], self.__heapList[self.__parent(index)] \
                = self.__heapList[self.__parent(index)],self.__heapList[index]
            index = self.__parent(index)

    # 查看堆中最大元素
    def findMax(self):
        if self.getSize() == 0:
            raise Exception("Cannot findMax when heap is empty")
        return self.__heapList[0]

    # 取出堆中最大元素
    # 移除的方法：Sift Down ，下沉法
    # 1.先将堆中最大的元素(即[0]位置元素) 与 堆末端元素(即[lenth-1]位置元素)交换位置
    # 2.删除[lenth-1]位置的元素
    # 3.将队首元素与左右子树中最大的元素比较，小于则互换，循环
    def extractMax(self):
        result = self.findMax()
        self.__heapList[0], self.__heapList[-1] = self.__heapList[-1], self.__heapList[0]
        self.__heapList.pop()
        self.__siftDown(0)

        return result

    def __siftDown(self, index):
        while self.__leftchild(index) < self.getSize():
            j = self.__leftchild(index)
            if j+1 < self.getSize() and self.__heapList[j+1] > self.__heapList[j]:
                j += 1
            # 现在的__heapList[j]是左右子树中的最大值
            if self.__heapList[j] <= self.__heapList[index]:
                break

            self.__heapList[index], self.__heapList[j] = self.__heapList[j], self.__heapList[index]
            index = j

    # replace操作 取出最大元素后放入一个新元素
    # 可以直接将堆顶元素替换以后sift down，一次O(logn)操作
    def replace(self, e):
        result = self.findMax()
        self.__heapList.insert(0, e)
        self.__siftDown(0)
        return result





if __name__ == '__main__':
    n = 1000000
    from time import time

    start_time1 = time()
    max_heap = MaxHeap()
    from random import randint
    for i in range(n):
        max_heap.add(randint(0, 1000))
    # for i in range(n):
    #     res = max_heap.extractMax()
    print('heap add: ', time() - start_time1) # heap add:  5.539180278778076


    # heapify的方式添加
    testList = []
    for i in range(n):
        testList.append(randint(0, 1000))
    start_time2 = time()
    max_heap2 = MaxHeap(testList)
    print('heapify add: ', time() - start_time2) # heapify add:  1.8540711402893066
