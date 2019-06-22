from arithmetic.LinkedList import LinkedList
from arithmetic.MySet.base import SetBase

class LinkedListSet(SetBase):
    def __init__(self):
        self.linkedlist_set = LinkedList()

    def isEmpty(self):
        return self.linkedlist_set.isEmpty()

    def getSize(self):
        return self.linkedlist_set.getSize()

    def contains(self, e):
        return self.linkedlist_set.contains(e)

    def add(self, e):
        if not self.linkedlist_set.contains(e):
            self.linkedlist_set.addFirst(e)

    def remove(self, e):
        self.linkedlist_set.remove(e)


if __name__ == "__main__":

    words = ""
    with open("shakespeare.txt", "r") as f:
        words = f.read()
    words = words.split()

    from time import time
    start_time = time()
    bst_set = LinkedListSet()
    for word in words:
        bst_set.add(word)

    print("Total words: ", len(words))
    print("Unique words: ", bst_set.getSize())
    print('Contains word "they": ', bst_set.contains("they"))
    print("Total time {} seconds".format(time() - start_time))