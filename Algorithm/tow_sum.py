# -*- coding=utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            for j in nums:
                if i + j == target:
                    print(i, j)


if __name__ == '__main__':
    solution = Solution()
    solution.twoSum([2, 7, 8, 9], 9)
