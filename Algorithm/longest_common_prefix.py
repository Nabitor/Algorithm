# -*- coding:utf-8 -*-

"""
问题描述：Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = ''
        for t in zip(*strs):
            if not all(c==t[0] for c in t):
                break
            pre += t[0]
        return pre


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["ab", "ab"]))
