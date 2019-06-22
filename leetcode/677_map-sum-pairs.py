# 键值映射
# 实现一个 MapSum 类里的两个方法，insert 和 sum。
#
# 对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。
# 如果键已经存在，那么原来的键值对将被替代成新的键值对。
#
# 对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。
#
# 示例 1:
#
# 输入: insert("apple", 3), 输出: Null
# 输入: sum("ap"), 输出: 3
# 输入: insert("app", 2), 输出: Null
# 输入: sum("ap"), 输出: 5

class MapSum:

    class __Node():
        def __init__(self, value = 0):
            self.value = value
            self.next = dict()

    def __init__(self):
        self.__root = self.__Node()

    def insert(self, key, val):
        cur = self.__root
        for char in key:
            if char not in cur.next:
                cur.next[char] = self.__Node()
            cur = cur.next[char]
        cur.value = val

    def sum(self, prefix):
        cur = self.__root
        for char in prefix:
            if char not in cur.next:
                return 0
            cur = cur.next[char]
        return self.__sum(cur)

    def __sum(self, node):
        # if len(node.next) == 0:
        #     return node.value

        result = node.value
        for nextkey in node.next.keys():
            result += self.__sum(node.next[nextkey])

        return result