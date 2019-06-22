# 二分搜索树
# 1.二叉树
# 2.左子树永远小于根节点，右子树永远大于根节点
# 3.存储数据要有一定的可比性

from queue import Queue

class BST():
    class __Node():
        def __init__(self, e):
            self.e = e
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None  # 根节点
        self.size = 0     # 树的节点数

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def add(self, e):
        # if self.root is None:
        #     self.root = self.__Node(e)
        #     self.size += 1
        # else:
        #     self.__addElement(self.root, e)
        self.root = self.__addElement(self.root, e)

    # 向以node为根的二分搜索树中插入元素e，递归算法
    def __addElement(self, node, e):
        # # 终止条件
        # # 当数据已经存在(相同)或者为叶子节点的时候，插入，结束
        # if node.e == e:
        #     return
        # elif e < node.e and node.left is None:
        #     node.left = self.__Node(e)
        #     self.size += 1
        #     return
        # elif e > node.e and node.right is None:
        #     node.right = self.__Node(e)
        #     self.size += 1
        #     return
        #
        # # 非终止时，继续向下递归查询
        # # 因为等于的条件之前已经判断过了，所以不用在判断了
        # if e < node.e:
        #     self.__addElement(node.left, e)
        # else:
        #     self.__addElement(node.right, e)

        # 另一种简洁的写法
        if not node:
            self.size += 1
            return self.__Node(e)
        if node.e == e:
            return node
        elif e < node.e:
            node.left = self.__addElement(node.left, e)
        else:
            node.right = self.__addElement(node.right, e)

        return node

    # 看二分搜索树中是否包含元素e,递归
    def contains(self, e):
        return self.__myContains(self.root, e)

    def __myContains(self, node, e):
        if node is None:
            return False

        if node.e == e:
            return True
        elif e < node.e:
            return self.__myContains(node.left, e)
        elif e > node.e:
            return self.__myContains(node.right, e)

    # 二叉树的前序遍历(先根遍历，根左右)
    def preOrder(self):
        self.__mypreOrder(self.root)

    # 前序遍历以node为根的二分搜索树，递归算法
    def __mypreOrder(self, node):
        if node is None:
            return
        print(node.e)
        self.__mypreOrder(node.left)
        self.__mypreOrder(node.right)

    # 二叉树的中序遍历(左根右)
    # 对二分搜索树从小到大排序
    def inOreder(self):
        self.__myinOrder(self.root)

    # 中序遍历以node为根的二分搜索树，递归算法
    def __myinOrder(self, node):
        if node is None:
            return
        self.__myinOrder(node.left)
        print(node.e)
        self.__myinOrder(node.right)

    # 二叉树的后序遍历(左右根)
    # 典型应用于内存的释放
    def postOrder(self):
        self.__mypostOrder(self.root)

    # 后序遍历以node为根的二分搜索树，递归算法
    def __mypostOrder(self, node):
        if node is None:
            return
        self.__mypostOrder(node.left)
        self.__mypostOrder(node.right)
        print(node.e)

    # 非递归的前序遍历
    def preOrderNR(self):
        stack = []
        stack.append(self.root)
        while len(stack) > 0:
            node = stack.pop()
            print(node.e)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    # 层序遍历(是广度优先遍历)
    # 层序遍历利用队列进行遍历
    def levelOrder(self):
        q = Queue()
        q.put(self.root)
        while not q.empty():
            node = q.get()
            print(node.e)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)

    # 查找二分搜索树中最小元素，递归写法__mymimum()
    def minmum(self):
        if self.size == 0:
            raise Exception("BST is empty")
        return self.__myminmum(self.root).e

    def __myminmum(self, node):
        if node.left is None:
            return node
        return self.__myminmum(node.left)

    # 查找二分搜索树中最大元素，非递归写法
    def maxmum(self):
        if self.root is None:
            return "BST is empty"
        node = self.root
        while node.right is not None:
            node = node.right
        return node.e

    # 从二分搜索树删除最小值所在的节点，返回最小值
    def removeMin(self):
        result = self.minmum()
        self.root = self.__myremoveMin(self.root)
        return result

    # 递归的删除以node为根的二叉树中的最小节点
    # 返回删除节点后的新二叉树的根
    def __myremoveMin(self, node):
        if node.left is None:
            rightNode = node.right
            node.right = None
            self.size -= 1
            return rightNode
        node.left = self.__myremoveMin(node.left)
        return node

    # 从二分搜索树中删除最大值所在的节点，返回最大值
    def removeMax(self):
        # 递归的删除以node为根的二叉树中的最小节点
        # 返回删除节点后的新二叉树的根
        def __myremove(node):
            if node.right is None:
                left = node.left
                node.left = None
                self.size -= 1
                return left
            node.right = __myremove(node.right)
            return node
        result = self.maxmum()
        self.root = __myremove(self.root)
        return result




    # 前序遍历打印输出二分搜索树
    def __str__(self):
        result = ""
        result = self.__generateBSTString(self.root, 0, result)
        return result

    # 生成以node为根节点，深度为depth的描述二叉树的字符串
    def __generateBSTString(self, node, depth, res):
        if node is None:
            res += "--" * depth + "None\n"
            return res
        res += "--" * depth + str(node.e) + "\n"
        res = self.__generateBSTString(node.left, depth+1, res)
        res = self.__generateBSTString(node.right, depth+1, res)

        return res

    # 删除二分搜索树中的任意节点
    def remove(self, e):
        # 递归的删除以node为根的二叉树中的节点e
        # 返回删除节点后的新二叉树的根
        def __myremove(node, e):
            # 1.如果传入的节点本身为空，直接返回
            if node is None:
                return
            # 2.如果待删除e小于node节点，递归左子树
            if e < node.e:
                node.left = __myremove(node.left, e)
                return node
            # 3.如果待删除e大于node节点，递归右子树
            elif e > node.e:
                node.right = __myremove(node.right, e)
                return node
            # 4.找到待删除的节点
            else: # e == node.e
                # (1).如果待删除的节点没有左子树，将右子树接上
                if node.left is None:
                    rightNode = node.right
                    node.right = None
                    self.size -= 1
                    return rightNode
                # (2).如果待删除的节点没有右子树，将左子树接上
                if node.right is None:
                    leftNode = node.left
                    node.left = None
                    self.size -= 1
                    return leftNode
                # (3).如果待删除的节点左右子树都存在，找到待删除节点的前驱节点(其左子树中最大的节点)
                #     或者后继节点(其右子树的最小节点)
                #     用这个节点顶替待删除节点的位置
                successor = self.__myminmum(node.right)
                successor.right = self.__myremoveMin(node.right)
                successor.left = node.left
                node.left = node.right = None
                return successor

        self.root = __myremove(self.root, e)






# if __name__ == "__main__":
#     bst = BST()
#     nums = [5,3,6,8,4,2]
#     for n in nums:
#         bst.add(n)
#     bst.remove(5)

    # print("递归先序遍历")
    # bst.preOrder()
    # print("非递归先序遍历")
    # bst.preOrderNR()
    # print("递归中序遍历")
    # bst.inOreder()
    # print("递归后序遍历")
    # bst.postOrder()
    # print("层序遍历")
    # bst.levelOrder()
    # print(bst)
    #
    # print(bst.removeMin())
    # print(bst.removeMax())
    # print(bst)
    # print(bst.minmum())
    # print(bst.maxmum())
