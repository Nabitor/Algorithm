# coding=utf-8

'''
问题描述：Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
'''


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        使用位操作Bit Manipulation来解的，用到了异或操作的特性，
        那么思路是既然0到n之间少了一个数，
        我们将这个少了一个数的数组合0到n之间完整的数组异或一下，
        那么相同的数字都变为0了，剩下的就是少了的那个数字了
        """
        result = 0
        for index in range(len(nums)):
            result ^= (index+1)^nums[index]

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.missingNumber([0]))
