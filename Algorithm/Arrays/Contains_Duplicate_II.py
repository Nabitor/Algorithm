# coding=utf-8

'''
问题描述：Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_dict = {}

        for index in range(len(nums)):
            idx = nums_dict.get(nums[index])

            if idx >= 0 and index - idx <= k:
                return True

            nums_dict[nums[index]] = index

        return False
