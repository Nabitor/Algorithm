# coding=utf-8
'''
问题描述：Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_, cnt = 0, 0
        for index in nums:
            if index == 0:
                cnt = 0
            else:
                cnt += 1

            sum_ = sum_ if sum_ > cnt else cnt

        return sum_


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxConsecutiveOnes([1, 1, 1, 0, 1, 1, 1, 1]))
