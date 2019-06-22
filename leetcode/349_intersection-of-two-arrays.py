# 两个数组的交集
# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1:
#
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2]
# 示例 2:
#
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [9,4]
# 说明:
#
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。
class Solution:
    # 1.将第一个列表放入set1
    # 2.遍历列表二，判断当前元素是否存在于set1中
    #   若存在，添加到返回列表中，将set1中的该元素移除
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        reslist = []
        for num in nums2:
            if set1.__contains__(num):
                reslist.append(num)
                set1.remove(num)

        return reslist