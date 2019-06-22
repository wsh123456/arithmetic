"""
删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 使用虚拟头节点
class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyHead = ListNode(-1)
        dummyHead.next = head

        prev = dummyHead
        while prev.next is not None:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummyHead.next


# 不使用虚拟头节点
class Solution2:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head is not None and head.val == val:
            head = head.next

        if head is None:
            return None

        current = head
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head


# 使用链表递归的解决删除
# 递归调用本身的代价：
#     函数调用 + 系统栈空间
#         函数的调用会占用时间资源，比如寻找函数所在位置
#         系统栈一直压入会满，当递归多次后就会出栈满错误
class Solution3:
    def removeElements(self, head, val):

        if head is None:
            return None

        result = self.removeElements(head.next, val)
        if head.val == val:
            return result
        else:
            head.next = result
            return head
