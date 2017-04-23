# -*- coding=utf-8 -*-
"""
    问题描述：Given a sorted array and a target value,
    return the index if the target is found. If not,
    return the index where it would be if it were inserted in order.

    You may assume no duplicates in the array.
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] >= target:
                break
            i += 1

        return i


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1,3,5,6], 7))
