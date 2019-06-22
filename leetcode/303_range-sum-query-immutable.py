# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
#
# 示例：
#
# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
#   说明:
#   你可以假设数组不可变。
#   会多次调用 sumRange 方法。


# 方法一：暴力破解。。结果会超时
class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, i, j):
        res = 0
        while i <= j:
            res = res + self.nums[i]
            i += 1
        return res


# 方法二：线段树
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

        def __leftchild(self, index):
            return 2 * index + 1

        def __rightchild(self, index):
            return 2 * index + 2

    def __init__(self, nums):
        if len(nums) > 0:
            self.seg = self.SegmentTree(nums)

    def sumRange(self, i, j):
        return self.seg.query(i, j)


# 迭代求和方式
import itertools
class NumArray2:

    def __init__(self, nums):
        # nums = [1,2,3,4]
        # _data = [1,3,6,10]
        self._data = list(itertools.accumulate(nums))

    def sumRange(self, i, j):
        return self._data[j] - self._data[i - 1] if i else self._data[j]
