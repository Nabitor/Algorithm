# coding:utf-8
"""
    问题描述：
    Determine whether an integer is a palindrome. Do this without extra space.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        _x = str(x)
        l = len(_x)

        for i in range(l//2):
            if _x[i] != _x[l-i-1]:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(12))
