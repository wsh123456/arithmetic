"""
leetcode:20
括号匹配
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

"""

class Solution():
    def isValid(self, s):
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")" or i == "]" or i == "}":
                if not stack:
                    return False
                outchar = stack.pop()
                if outchar == "(" and i != ")":
                    return False
                if outchar == "[" and i != "]":
                    return False
                if outchar == "{" and i != "}":
                    return False
        if len(stack) == 0:
            return True
        else:
            return  False

a = Solution()
a.isValid("{}{}")