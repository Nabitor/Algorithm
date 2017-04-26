# coding=utf-8
"""
    问题描述：Implement int sqrt(int x).
    Compute and return the square root of x.
    解题思路：使用二分法解题。
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start, end = 1, x
        while start + 1 < end:
            mid = (start + end) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid
        if end * end <= x:
            return end
        return start


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(0))
