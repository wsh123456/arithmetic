# 添加与搜索单词-数据结构设计

# 设计一个支持以下两种操作的数据结构：
# void addWord(word)
# bool search(word)
# search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

# 示例:
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true

# 说明:
# 你可以假设所有单词都是由小写字母 a-z 组成的

class WordDictionary:
    class __Node():
        def __init__(self, isword = False):
            self.isword = isword
            self.next = dict()

    def __init__(self):
        self.__root = self.__Node()

    def addWord(self, word):
        cur = self.__root
        for char in word:
            if char not in cur.next:
                cur.next[char] = self.__Node()
            cur = cur.next[char]
        cur.isword = True

    def search(self, word):
        return self.__match(self.__root, word, 0)

    def __match(self, node, word, index):
        if index == len(word):
            return node.isword

        char = word[index]
        if char != ".":
            if char not in node.next:
                return False
            return self.__match(node.next[char], word, index + 1)
        else:
            for nextkey in node.next.keys():
                if self.__match(node.next[nextkey], word, index + 1):
                    return True
            return False

