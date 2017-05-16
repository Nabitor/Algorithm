# coding=utf-8

'''
问题描述：Given a non-empty array of integers, return the third maximum number in this array.
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        设置三个变量，保存最大的，第二大的和第三大的，然后依次判断更新。
        '''
        # Int_Min = -2**32
        #
        # first, second, third = Int_Min, Int_Min, Int_Min
        #
        # for num in nums:
        #     if num > first:
        #         third, second, first = second, first, num
        #     elif second < num < first:
        #         second, third = num, second
        #     elif third < num < second:
        #         third = num
        #
        # return first if third == Int_Min or third == second else third
        # 上面这个居然能过 哈哈

        Int_Min = None

        first, second, third = Int_Min, Int_Min, Int_Min

        for num in nums:
            if first is None or num > first:
                third, second, first = second, first, num
            elif second is None or second < num:
                second, third = num, second
            elif third is None or third < num:
                third = num

        return third if third is not None else first



if __name__ == '__main__':
    solution = Solution()
    print(solution.thirdMax([1,2,-2147483648]))
