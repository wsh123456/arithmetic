# 用列表存储并查集的结构
# 用列表的索引来记录数据的id，里面的值即为数据所属的集合
# quick find 查询非常快速O(1)，但是合并集合效率很低O(n)

from arithmetic.UnionFind.UF import UF

class UnionFind1(UF):
    def __init__(self, size):
        self.id = [None] * size
        for i in range(len(self.id)):
            self.id[i] = i

    def getSize(self):
        return self.id.__len__()

    # 查找元素index所对应的集合的编号
    def __find(self, index):
        if index < 0 or index > len(self.id):
            raise Exception("index is out of bound")
        return self.id[index]

    # 查看元素p和元素q是否为同一个集合
    def isConnected(self, p, q):
        return self.__find(p) == self.__find(q)

    # 合并元素p和q的集合
    def unionElements(self,p ,q):
        pID = self.__find(p)
        qID = self.__find(q)

        if pID == qID:
            return

        for i in range(self.id):
            if self.id[i] == pID:
                self.id[i] = qID