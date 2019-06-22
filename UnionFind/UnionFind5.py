from arithmetic.UnionFind.UF import UF


# 第五版的并查集，使用递归的方法进行路径压缩
class UnionFind4(UF):
    def __init__(self, size):
        self.__parent = [None] * size
        self.sz = [1] * size  # sz[i]表示以i为根的集合中的元素个数
        for i in range(len(self.__parent)):
            self.__parent[i] = i

    def getSize(self):
        return len(self.__parent)

    # 查找过程，查找元素p 对应的集合编号,递归返回父亲节点
    def __find(self, p):
        if p < 0 or p > len(self.__parent):
            raise Exception("p is out of bound")
        if self.__parent[p] != p:
            # 如果该节点不是根节点，就返回他的父亲节点直到根
            self.__parent[p] = self.__find(self.__parent[p])
        return self.__parent[p]

    def isConnected(self, p, q):
        return self.__find(p) == self.__find(q)

    # 合并p和q所在的集合
    # O(h)复杂度，h为树的高度
    def unionElements(self, p, q):
        pRoot = self.__find(p)
        qRoot = self.__find(q)
        if pRoot == qRoot:
            return

        # 根据两棵树上元素个数判断合并方向，将元素个数少的合并到多的集合
        if pRoot < qRoot:
            self.__parent[pRoot] = qRoot
            # self.sz[pRoot] = self.sz[qRoot]  这里并不需要维护，因为qRoot就是根节点而且就是最大的
        elif pRoot > qRoot:
            self.__parent[qRoot] = pRoot
            # self.sz[qRoot] = self.sz[pRoot]
        else:  # pRoot == qRoot
            self.__parent[qRoot] = self.__parent[pRoot]
            self.sz[pRoot] = self.sz[pRoot] + 1

