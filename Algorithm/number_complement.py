# coding=utf-8
"""
    问题描述：Given a positive integer, output its complement number.
    The complement strategy is to flip the bits of its binary representation.
    解题思路：1、对于这个整数num，转换成对应的二进制表示，这个二进制表示共有x位（不高于32）
    2、将这x位取反后，得到对应的10进制值就是结果。
"""


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num
