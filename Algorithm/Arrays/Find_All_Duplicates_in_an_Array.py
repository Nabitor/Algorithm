# coding=utf-8

'''
问题描述：Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        '''
        负号标记法。
        '''
        result = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                result.append(abs(num))
            else:
                nums[abs(num)-1] *= -1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findDuplicates([4,3,2,7,8,2,3,1]))
