#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-20 15:34:18
# @Author  : xuejun (xuemyjun@gmail.com)

"""
Given a string, find the length of the longest substring without
repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, length = -1, 0
        _hash = {}
        for i in range(len(s)):
            left = max(left, _hash.get(s[i], -1))
            _hash[s[i]] = i
            length = max(length, i - left)

        return length


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
