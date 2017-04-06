# -*- coding=utf-8 -*-

"""
问题描述：Given an array of integers,
    find two numbers such that they add up to a specific target number.
解题思路：第一次遍历数组先将所有元素和它的下标作为key-value对存入Hashmap中，
    第二次遍历数组时根据目标和与当前元素之差，在Hashmap中找相应的差值。
    如果存在该差值，说明存在两个数之和是目标和。
    此时记录下当前数组元素下标并拿出Hashmap中数组元素下标即可。
    Hashmap获取元素的时间复杂度是O(1)，所以总的时间复杂度仍不超过O(n)。
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 8, 9], 9))
