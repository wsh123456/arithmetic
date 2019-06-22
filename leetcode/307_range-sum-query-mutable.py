# 区域和检索，数组可修改

# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
#
# update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。
#
# 示例:
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# 说明:
# 数组仅可以在 update 函数下进行修改。
# 你可以假设 update 函数与 sumRange 函数的调用次数是均匀分布的。


class NumArray1:
    class SegmentTree():
        def __init__(self, arr):
            # 获取构建线段树所需的h
            def getH(myarr):
                h = 0
                length = len(myarr) - 1
                while length >= 1 and len(myarr) != 1:
                    length = length // 2
                    h += 1
                return h

            self.__data = arr
            self.__tree = [None] * int(4 * 2 ** (getH(arr) - 1))

            # 构建一棵线段树
            self.__buildSegmentTree(0, 0, len(self.__data) - 1)

        # 在treeIndex的位置创建表示区间[left...right]的线段树
        def __buildSegmentTree(self, index, left, right):
            # 终止条件，添加到叶子节点
            if left == right:
                self.__tree[index] = self.__data[left]
                return

            leftIndex = self.__leftchild(index)
            rightIndex = self.__rightchild(index)
            mid = left + (right - left - 1) // 2

            self.__buildSegmentTree(leftIndex, left, mid)
            self.__buildSegmentTree(rightIndex, mid + 1, right)
            self.__tree[index] = self.__tree[leftIndex] + self.__tree[rightIndex]

        # 返回区间 [queryL, queryR] 的值
        def query(self, queryL, queryR):
            if queryL < 0 or queryR < 0 or queryL > len(self.__data) or queryR > len(self.__data) or queryL > queryR:
                raise Exception("Index is illegal")
            return self.__query(0, 0, len(self.__data) - 1, queryL, queryR)

        # 在以index为根节点的线段树中[left...right]的范围里，搜索区间[queryL...queryR]的值
        def __query(self, index, left, right, queryL, queryR):
            if left == queryL and right == queryR:
                return self.__tree[index]
            mid = left + (right - left - 1) // 2
            leftChild = self.__leftchild(index)
            rightChild = self.__rightchild(index)
            if queryL > mid:
                return self.__query(rightChild, mid + 1, right, queryL, queryR)
            elif queryR <= mid:
                return self.__query(leftChild, left, mid, queryL, queryR)

            leftResult = self.__query(leftChild, left, mid, queryL, mid)
            rightResult = self.__query(rightChild, mid + 1, right, mid + 1, queryR)
            return leftResult + rightResult

        def set(self, index, e):
            if index < 0 or index >= len(self.__data):
                raise Exception("Index is illegal")
            self.__data[index] = e
            self.__set(0, 0, len(self.__data) - 1, index, e)

        # 在以treeIndex为根节点的线段树中，更新index位置的元素
        def __set(self, treeIndex, left, right, index, e):
            if left == right:
                self.__tree[treeIndex] = e
                return
            mid = left + (right - left - 1) // 2
            leftChild = self.__leftchild(treeIndex)
            rightChild = self.__rightchild(treeIndex)
            if mid < index:
                self.__set(rightChild, mid + 1, right, index, e)
            else:  # mid >= index
                self.__set(leftChild, left, mid, index, e)
            self.__tree[treeIndex] = self.__tree[leftChild] + self.__tree[rightChild]

        def __leftchild(self, index):
            return 2 * index + 1

        def __rightchild(self, index):
            return 2 * index + 2

    def __init__(self, nums):
        if len(nums) > 0:
            self.seg = self.SegmentTree(nums)

    def update(self, i, val):
        self.seg.set(i, val)

    def sumRange(self, i, j):
        return self.seg.query(i, j)