# -*- coding=utf-8 -*-
"""
LeetCode: 258 Add Digits
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
解题思路：
    1、这道题让我们求数根，所谓数根，就是将大于10的数的各位上的数字相加，若结果还是大于0的话，则继续相加，指导
    数字小于10为止。
    2、先看看一些规律
        1    1
        2    2
        3    3
        4    4
        5    5
        6    6
        7    7
        8    8
        9    9
        10    1
        11    2
        12    3
        13    4
        14    5
        15    6
        16    7
        17    8
        18    9
        19    1
        20    2
       每9个一循环，所有大于9的数的树根都是对9取余，那么对于等于9的数对9取余就是0了，不取0取9
"""

class Add_Digits(object):
    def add_digits_(self, num):
        """
        普通的方法。
        :type num: int
        :rtype: int
        """
        while num // 10:
            sum = 0
            while num > 0:
                sum += num % 10
                num /= 10
            num = sum

        return num


    def add_digits(self, num):
        """
        根据规律求解。
        :type num: int
        :rtype: int
        """
        return (num % 9 or 9) if num else 0


if __name__ == '__main__':
    ad = Add_Digits()
    print(ad.add_digits_(38))
