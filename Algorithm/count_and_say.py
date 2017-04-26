# coding=utf-8
"""
    问题描述：The count-and-say sequence is the sequence of integers beginning as follows:
    1, 11, 21, 1211, 111221, ...

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.
    Given an integer n, generate the nth sequence.

    Note: The sequence of integers will be represented as a string

    解释一下就是，输入n，那么我就打出第n行的字符串。
    怎么确定第n行字符串呢？他的这个是有规律的。
    n = 1时，打印一个1。
    n = 2时，看n=1那一行，念：1个1，所以打印：11。
    n = 3时，看n=2那一行，念：2个1，所以打印：21。
    n = 4时，看n=3那一行，念：一个2一个1，所以打印：1211。
    以此类推。(注意这里n是从1开始的）
    所以构建当前行的字符串要依据上一行的字符串。“小陷阱就是跑完循环之后记得把最后一个字符也加上，因为之前只是计数而已。”

    解题思路：
    逐个构建序列——根据第i-1个序列构建后第i个。理解题目意思后便知道在扫描前一个序列ret时，
    需要一个计数变量count记录当前字符重复的次数，以及需要一个字符变量prev记录上一个字符的值。
    当ret[i] = prev，则先不写入结果，而增加count。
    当ret[i] != prev时，说明prev的重复结束，需要将count和prev都写入结果，然后重置count为1，prev为ret[i]。
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            count = 1
            temp = []
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index-1])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s
