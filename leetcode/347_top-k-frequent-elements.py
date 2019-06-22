# 前K个高频元素
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
# 说明：
#
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
import heapq

class Solution:
    class Freq():
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __lt__(self, other):
            return self.value < other.value

        def __eq__(self, other):
            return self.value == other.value

        def __str__(self):
            return str(self.key) + ":" + str(self.value)

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numHeap = []
        numDict = {}
        # 将传进来的数组按照出现次数添加为 值：频率 字典
        for num in nums:
            if numDict.__contains__(num):
                numDict[num] += 1
            else:
                numDict.setdefault(num, 1)

        # 循环每一个key，将键值对存入对象Freq，在添加进堆中
        for key in numDict.keys():
            if len(numHeap) < k:
                heapq.heappush(numHeap, self.Freq(key, numDict[key]))
            elif numDict[key] > numHeap[0].value:
                heapq.heappop(numHeap)
                heapq.heappush(numHeap, self.Freq(key, numDict[key]))
        numHeap.sort(reverse=True)

        resultHeap = []
        for i in range(len(numHeap)):
            resultHeap.append(numHeap[i].key)
        return resultHeap


# 写法看着很简洁
class Solution2:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        Dict = {}
        for i in range(len(nums)):
            if nums[i] in Dict:
                Dict[nums[i]] = Dict[nums[i]] + 1
            else:
                Dict[nums[i]] = 1

        output = sorted(Dict.items(), key=lambda e: e[1], reverse=True)

        final = []
        for i in range(k):
            final.append(output[i][0])
        return final



if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3,3,3,3], 2))
