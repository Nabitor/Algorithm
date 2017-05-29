# coding=utf-8

'''
问题描述：Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        用打擂台的方法，遇见相同的+1，遇见不同的-1，最后剩下的就是多出来的数。
        '''
        candidate, count = None, 0

        for num in nums:
            if count == 0:
                candidate, count = num, 1
            elif candidate == num:
                count += 1
            else:
                count -= 1

        return candidate
