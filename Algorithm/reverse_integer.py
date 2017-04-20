# -*- coding=utf-8 -*-
"""
    问题描述：Reverse digits of an integer.

    Example1: x = 123, return 321
    Example2: x = -123, return -321

    The input is assumed to be a 32-bit signed integer.
    Your function should return 0 when the reversed integer overflows.
"""
import sys
import os


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(abs(x))
        _x_str = x_str[::-1]
        _x = int(_x_str)
        if _x > 2147483648:
            return 0
        else:
            if x < 0:
                return -1*_x
            else:
                return _x



if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(-123))
