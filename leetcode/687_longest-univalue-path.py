# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
# 注意：两个节点之间的路径长度由它们之间的边数表示。
# 示例 1:
# 输入:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# 输出: 2

# 示例 2:
# 输入:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# 输出: 2
# 注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 分别找到某个节点的左子树和右子树中的最大路径
# 之后会有两种情况
# 1.左右子树形成最大路径
# 2.左右子树中的最大值与父亲节点形成最大路径

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.rtype = 0
        self.__mylongest(root, -1)
        return self.rtype

    def __mylongest(self, node, e):
        if not node:
            return 0
        left = self.__mylongest(node.left, node.val)
        right = self.__mylongest(node.right, node.val)
        self.rtype = max(self.rtype ,left + right)
        return max(left, right) + 1 if node.val == e else 0



def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            # line = next(lines)
            line = "[0,0,,8,1,1,1,1,1,9,2,3,3,3,1,1,1,1,1,1,3,3,3,1,9,9,3,3,3,3,3,4,4]"
            root = stringToTreeNode(line)

            ret = Solution().longestUnivaluePath(root)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()






