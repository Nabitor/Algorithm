# coding=utf-8

'''
问题描述：Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Time Limit Exceeded
        # max_profit = 0
        # for index in range(len(prices)-1):
        #     max_ = max(prices[index+1:])
        #     max_profit = max_ - prices[index] \
        #         if max_ > prices[index] and max_profit < max_ - prices[index] else max_profit
        #
        #
        # return max_profit

        '''
        从前往后遍历数据，找出最小的买入价格，同时每次更新卖出价格同最低价格之差即可。
        '''
        if len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if min_price > price:
                min_price = price

            if max_profit < price - min_price:
                max_profit = price - min_price

        return max_profit


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
