# Set 集合
# 典型应用：访问客户的统计，词汇量统计
# 有序的集合大多基于搜索树(二分搜索树，平衡二叉树(红黑树))实现
# 无序的集合可基于哈希表实现

from arithmetic.Binary_Search_Tree.BST import BST
from arithmetic.MySet.base import SetBase


class BSTSet(SetBase):
    def __init__(self):
        self.bst_set = BST()

    def getSize(self):
        return self.bst_set.size

    def isEmpty(self):
        return self.bst_set.isEmpty()

    def add(self, e):
        self.bst_set.add(e)

    def contains(self, e):
        return self.bst_set.contains(e)

    def remove(self, e):
        self.bst_set.remove(e)


if __name__ == "__main__":

    words = ""
    with open("shakespeare.txt", "r") as f:
        words = f.read()
    words = words.split()

    from time import time
    start_time = time()
    bst_set = BSTSet()
    for word in words:
        bst_set.add(word)

    print("Total words: ", len(words))
    print("Unique words: ", bst_set.getSize())
    print('Contains word "they": ', bst_set.contains("they"))
    print("Total time {} seconds".format(time() - start_time))