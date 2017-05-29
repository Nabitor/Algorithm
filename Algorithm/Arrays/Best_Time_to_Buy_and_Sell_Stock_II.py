# coding=utf-8

'''
问题描述：Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        '''
        解题思路：计算每个相邻的diff差，只要diff大于0，就累积起来。
        '''
        if not prices:
            return 0

        max_profit = 0
        for index in range(1, len(prices)):
            diff = prices[index] - prices[index-1]
            max_profit += diff if diff > 0 else 0

        return max_profit


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([2,1,2,0,4]))
