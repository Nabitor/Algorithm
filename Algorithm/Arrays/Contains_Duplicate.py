# coding=utf-8

'''
问题描述：Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
'''


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_ = set(nums)

        if len(nums) == len(nums_):
            return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsDuplicate([1, 2, 1, 3]))
