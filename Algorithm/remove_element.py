# coding=utf-8

"""
    问题描述：Given an array and a value, remove all instances of that value in place and return the new length.
    Do not allocate extra space for another array, you must do this in place with constant memory.
    The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for index in range(len(nums)):
            if nums[index] == val:
                count += 1
            else:
                nums[index - count] = nums[index]

        return len(nums) - count


if __name__ == '__main__':
    solution = Solution()
    printsolution.removeElement([3, 2, 2, 3], 2)
