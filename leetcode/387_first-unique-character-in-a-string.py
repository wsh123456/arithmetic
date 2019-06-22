# 字符串中的第一个唯一字符
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
# 案例:
#
# s = "leetcode"
# 返回 0.
#
# s = "loveleetcode",
# 返回 2.

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = dict()
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq.setdefault(c, 1)
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1