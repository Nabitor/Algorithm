# -*- coding=utf-8 -*-
"""
Given an array of integers, every element appears twice
except for one. Find that single one.
解题思路：
    1、先对元素进行排序，然后进行相邻两元素的对比，如a1和a2对比，
    a3和a4对比，如果不同，则前一个元素(a1、a3)就是所要查找的元素
    2、利用XOR运算，因为A XOR A = 0，且XOR运算是可交换的，于是，
    对于实例{2,1,4,5,2,4,1}就会有这样的结果：
    (2^1^4^5^2^4^1) => ((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5
"""


class Solution(object):
    def single_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]

        return result

    def single_number_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i] != nums[i - 1]:
                return nums[i - 1]

            return nums[-1]


def main():
    solution = Solution()
    print(solution.single_number_2([1, 2, 1, 2, 4]))


if __name__ == '__main__':
    main()
