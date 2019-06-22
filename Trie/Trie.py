class Trie():
    class __Node():
        def __init__(self, isword = False):
            self.isword = isword
            self.next = dict()

    def __init__(self):
        self.__root = self.__Node()
        # 此处的 size 指的是单词数，而非节点数
        self.__size = 0

    # 获取trie中的单词数
    def getSize(self):
        return self.__size

    # 向trie中添加单词
    def add(self, word):
        cur = self.__root
        for char in word:
            if char not in cur.next:
                cur.next[char] = self.__Node()
            cur = cur.next[char]
        if not cur.isword:
            cur.isword = True
            self.__size += 1

    # 在trie中查询是否存在 word
    def contains(self, word):
        cur = self.__root
        for char in word:
            if char not in cur.next:
                return False
            cur = cur.next[char]

        return cur.isword

    # 查找trie中是否包含含有 prefix 为前缀的单词 (prefix 前缀)
    def ifPrefix(self, prefix):
        cur = self.__root
        for char in prefix:
            if char not in cur.next:
                return False
            cur = cur.next[char]
        return True


trie = Trie()
trie.add("words")
trie.add("word")
print(trie.contains("word"))
print(trie.ifPrefix("wo"))
print(trie.getSize())