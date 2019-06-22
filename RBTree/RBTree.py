RED = True
BLACK = False

class RBTree():
    class __Node():
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.color = RED

    def __init__(self):
        self.__root = None
        self.__size = 0

    # 判断节点颜色，主要针对空节点视为黑色
    def __isRed(self, node):
        if node is None:
            return BLACK
        return node.color

    # 向红黑树中添加元素，递归
    def add(self, key, value):
        self.__root = self.__addR(self.__root, key, value)
        self.__root.color = BLACK  # 完成添加后保持根节点为黑色
    def __addR(self, node, key, value):
        if node is None:
            self.__size += 1
            return self.__Node(key, value)
        if key < node.key:
            node.left = self.__addR(node.left, key, value)
        elif key > node.key:
            node.right = self.__addR(node.right, key, value)
        else: # key == node.key
            node.value = value
        # 再添加完成后需要对节点进行调整具体分为三种情况
        # 1.向二节点或三节点的右子树添加节点，右子树为 红 ，左子树节点如果不为红(空返回BLACK)
        #   对节点node 进行左旋转操作
        #         45
        #       /
        #     25(r)
        #       \
        #       30(r)
        if self.__isRed(node.right) and not self.__isRed(node.left):
            node = self.__leftRotate(node)
        # 2.对完成第一步的情况，和本身添加就添加到三节点的左树情况
        #           45
        #          /
        #        30(r)
        #       /
        #     25(r)
        #   对45进行一次右旋转
        if self.__isRed(node.left) and self.__isRed(node.left.left):
            node = self.__rightRotate(node)
        # 3.对node的左右节点都为红色的情况，进行颜色的翻转
        #          30
        #        /    \
        #      25(r)  45(r)
        if self.__isRed(node.left) and self.__isRed(node.right):
            self.__flipColors(node)
        return node

    # 对 node 节点进行左旋转操作，返回新的节点
    #           node                                 x
    #          /   \                               /  \
    #        T1     x         左旋转            node   T3
    #             /  \      ---------->        / \
    #           T2   T3                     T1   T2
    def __leftRotate(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        # 旋转完成后，进行颜色的调整
        x.color = node.color
        node.color = RED
        return x

    # 针对添加后形成暂时的四节点，进行颜色翻转
    def __flipColors(self, node):
        node.color = RED
        node.left.color = node.right.color = BLACK

    # 对 node 节点进行右旋转操作，返回新的节点
    #           node                                 x
    #          /   \                               /   \
    #        x     T2         右旋转             y     node
    #      /  \             ---------->                / \
    #     y   T1                                     T1  T2
    def __rightRotate(self, node):
        x = node.left
        node.left = x.right
        x.right = node

        x.color = node.color
        node.color = RED
        # 旋转完成后形成新的暂时四节点，之后进行颜色翻转
        return x


if __name__ == "__main__":
    rbt = RBTree()
    listT = [5,6,2,3,5,567,345,23]
    for i in range(len(listT)):
        rbt.add(listT[i], listT[i])