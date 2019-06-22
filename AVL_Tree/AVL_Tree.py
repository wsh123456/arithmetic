# node节点存储的是 键值对的avl树，以key的值为准
class AVLTree():
    class __Node():
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.right = self.left = None
            self.height = 1

    def __init__(self):
        self.__root = None
        self.__size = 0

    # 传入一个节点，返回该节点的高度
    def __getHeight(self, node):
        if node is None:
            return 0
        return node.height

    # 获取节点的平衡因子
    def __getBalanceFactor(self, node):
        if node is None:
            return 0
        return self.__getHeight(node.left) - self.__getHeight(node.right)

    # 向树中添加节点，递归，更新height值
    def add(self, key, value): self.__root = self.__addR(self.__root, key, value)
    def __addR(self, node, key, value):
        if node is None:
            self.__size += 1
            return self.__Node(key, value)
        if key > node.key:
            node.right = self.__addR(node.right, key, value)
        elif key < node.key:
            node.left = self.__addR(node.left, key, value)
        else:
            node.value = value

        node.height = 1 + max(self.__getHeight(node.left), self.__getHeight(node.right))
        if abs(self.__getBalanceFactor(node)) > 1:
            print("unbalance")
        # LL
        if self.__getBalanceFactor(node) > 1 and self.__getBalanceFactor(node.left) >= 0:
            return self.__rightRotate(node)
        # RR
        if self.__getBalanceFactor(node) < -1 and self.__getBalanceFactor(node.right) <= 0:
            return self.__leftRotate(node)
        # LR
        if self.__getBalanceFactor(node) > 1 and self.__getBalanceFactor(node.left) < 0:
            node.left = self.__leftRotate(node.left)
            return self.__rightRotate(node)
        # RL
        if self.__getBalanceFactor(node) < -1 and self.__getBalanceFactor(node.right) > 0:
            node.right = self.__rightRotate(node.right)
            return self.__leftRotate(node)

        return node

    # 右旋转操作，返回新的平衡树的根节点
    #            y                                   x
    #          /   \                               /   \
    #        x     T4       y 向右旋转           z       y
    #      /  \             ---------->        / \      / \
    #     z    T3                             T1  T2   T3  T4
    #    / \
    #  T1  T2
    def __rightRotate(self, y):
        x = y.left
        T3 = y.left.right

        y.left = T3
        x.right = y

        y.height = max(self.__getHeight(y.left), self.__getHeight(y.right)) + 1
        x.height = max(self.__getHeight(x.left), self.__getHeight(x.right)) + 1
        return x

    # 左旋转操作，返回新的平衡树的根节点
    #            y                                   x
    #          /   \                               /   \
    #        T1     x       y 向左旋转           y      z
    #              /  \     ---------->        / \      / \
    #            T2    z                     T1  T2   T3  T4
    #                 / \
    #               T3  T4
    def __leftRotate(self, y):
        T2 = y.right.left
        x = y.right

        y.right = T2
        x.left = y

        y.height = max(self.__getHeight(y.left), self.__getHeight(y.right)) + 1
        x.height = max(self.__getHeight(x.left), self.__getHeight(x.right)) + 1
        return x

    # 删除某节点
    def remove(self, key): self.__remove(self.__root, key)
    def __remove(self, node, key):
        if node is None:
            return None
        retNode = None
        if key < node.key:
            node.left = self.__remove(node.left, key)
            retNode = node
        elif key > node.key:
            node.right = self.__remove(node.right, key)
            retNode = node
        else: # key==node.key
            # 待删除节点左子树为空
            if node.left is None:
                rightNode = node.right
                node.right = None
                self.__size -= 1
                retNode = rightNode
            # 待删除节点右子树为空
            elif node.right is None:
                leftNode = node.left
                node.left = None
                self.__size -= 1
                retNode = leftNode
            else:
                # 待删除节点左右子树均不为空，(前驱或后继)
                successor = self.__minimum(node.right)
                # successor.right = self.__removeMin(node.right) #会有问题，未进行平衡
                successor.right = self.__remove(node.right, successor.key)
                successor.left = node.left
                node.left = node.right = None
                retNode = successor

        if retNode is None:
            return
        retNode.height = 1 + max(self.__getHeight(retNode.left), self.__getHeight(retNode.right))
        # LL
        if self.__getBalanceFactor(retNode) > 1 and self.__getBalanceFactor(retNode.left) >= 0:
            return self.__rightRotate(retNode)
        # RR
        if self.__getBalanceFactor(retNode) < -1 and self.__getBalanceFactor(retNode.right) <= 0:
            return self.__leftRotate(retNode)
        # LR
        if self.__getBalanceFactor(retNode) > 1 and self.__getBalanceFactor(retNode.left) < 0:
            retNode.left = self.__leftRotate(retNode.left)
            return self.__rightRotate(retNode)
        # RL
        if self.__getBalanceFactor(retNode) < -1 and self.__getBalanceFactor(retNode.right) > 0:
            retNode.right = self.__rightRotate(retNode.right)
            return self.__leftRotate(retNode)

        return retNode




    def __minimum(self, node):
        if node.left is None:
            return node
        return self.__minimum(node.left)

    def __removeMin(self, node):
        if node.left is None:
            rightNode = node.right
            node.right = None
            self.__size -= 1
            return rightNode
        node.left = self.__removeMin(node.left)
        return node

    # 判断是否是一棵二分搜索树
    def isBST(self):
        keylist = []
        self.__inOrder(self.__root, keylist)
        for i in range(1, len(keylist)):
            if keylist[i - 1] > keylist[i]:
                return False
        return True

    # 中序递归
    def __inOrder(self, node, keys):
        if node is None:
            return
        self.__inOrder(node.left, keys)
        keys.append(node.key)
        self.__inOrder(node.right, keys)

    # 判断是否为一棵平衡二叉树
    def isBalanced(self):
        def __isBalanced(node):
            if node is None:
                return True
            balanceFactor = self.__getBalanceFactor(node)
            if abs(balanceFactor) > 1:
                return False
            return __isBalanced(node.left) and __isBalanced(node.right)

        return __isBalanced(self.__root)



if __name__ == "__main__":
    avl = AVLTree()
    listT = [5,6,2,3,5,567,345,23]
    for i in range(len(listT)):
        avl.add(listT[i], listT[i])

    avl.remove(5)

    print(avl.isBST())
    print(avl.isBalanced())