# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
#
# 示例:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");
# trie.search("app");     // 返回 true
# 说明:
#
# 你可以假设所有的输入都是由小写字母 a-z 构成的。
# 保证所有输入均为非空字符串。


class Trie:
    class __Node():
        def __init__(self, isword = False):
            self.isword = isword
            self.next = dict()

    def __init__(self):
        self.__root = self.__Node()

    # 向trie中添加单词
    def insert(self, word):
        cur = self.__root
        for char in word:
            if char not in cur.next:
                cur.next[char] = self.__Node()
            cur = cur.next[char]
        if not cur.isword:
            cur.isword = True

    # 在trie中查询是否存在 word
    def search(self, word):
        cur = self.__root
        for char in word:
            if char not in cur.next:
                return False
            cur = cur.next[char]
        return cur.isword

    # 查找trie中是否包含含有 prefix 为前缀的单词 (prefix 前缀)
    def startsWith(self, prefix):
        cur = self.__root
        for char in prefix:
            if char not in cur.next:
                return False
            cur = cur.next[char]
        return True