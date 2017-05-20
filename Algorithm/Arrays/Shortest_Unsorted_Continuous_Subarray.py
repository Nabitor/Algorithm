# coding=utf-8

'''
问题描述：Given an integer array, you need to find one continuous subarray
that if you only sort this subarray in ascending order,
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make
the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        解题方法：先对nums进行排序，然后同原列表进行比较，
        找出第一个不一样的以及最后一个不一样的位置即可。
        '''
        nums_sorted = sorted(nums)
        first, second = -1, -1
        for index in range(len(nums)):
            if nums[index] != nums_sorted[index]:
                if first == -1:
                    first = index
                second = index

        return second - first + 1 if first != second else 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
