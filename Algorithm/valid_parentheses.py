# coding=utf-8
"""
    问题描述：Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for index in range(len(s)):
            if s[index] in ["(", "[", "{"]:
                stack.append(s[index])
            elif s[index] in [")", "]", "}"]:
                if len(stack) == 0:
                    return False
                else:
                    s_ = stack.pop()
                    if (s_ == "(" and s[index] != ")") or (s_ == "[" and s[index] != "]") or (s_ == "{" and s[index] != "}"):
                        return False

        if len(stack) != 0:
            return False

        return True
