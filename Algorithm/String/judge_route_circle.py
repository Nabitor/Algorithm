#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-22 15:12:18
# @Author  : xuejun (xuemyjun@gmail.com)

"""
Initially, there is a Robot at position (0, 0).
Given a sequence of its moves, judge if this robot makes a circle,
which means it moves back to the original place.

The move sequence is represented by a string.
And each move is represent by a character.
The valid robot moves are
R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing
whether the robot makes a circle.

Example 1:

Input: "UD"
Output: true

Example 2:

Input: "LL"
Output: false

"""


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count("R") == moves.count("L")\
            and moves.count("U") == moves.count("D")


if __name__ == '__main__':
    solution = Solution()
    print(solution.judgeCircle("RLUURDDDLU"))
