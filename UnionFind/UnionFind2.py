from arithmetic.UnionFind.UF import UF

# 令孩子节点指向父亲节点，每次新union 的时候先找到当前的根节点，再将根节点指向新的根节点
class UnionFind2(UF):
    def __init__(self, size):
        self.__parent = [None] * size
        for i in range(len(self.__parent)):
            self.__parent[i] = i

    def getSize(self):
        return len(self.__parent)

    # 查找过程，查找元素p 对应的集合编号
    def __find(self, p):
        if p < 0 or p > len(self.__parent):
            raise Exception("p is out of bound")
        while self.__parent[p] != p:
            p = self.__parent[p]
        return p

    def isConnected(self, p, q):
        return self.__find(p) == self.__find(q)

    # 合并p和q所在的集合
    # O(h)复杂度，h为树的高度
    def unionElements(self,p ,q):
        pRoot = self.__find(p)
        qRoot = self.__find(q)
        if pRoot == qRoot:
            return
        self.__parent[pRoot] = qRoot
