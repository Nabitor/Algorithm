#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-02
# @Author  : xuejun (xj174850@163.com)
# @Link    : https://github.com/NeuObito


def insert_sort(nums):
    if not isinstance(nums, list):
        return

    num_len = len(nums)
    if num_len <= 1:
        return nums

    for index in range(1, num_len):
        num_index = nums[index]
        index_ = index - 1

        # 找到排序点从右遍历，可以减少遍历次数
        while index_ >= 0 and nums[index_] > num_index:
            nums[index_+1] = nums[index_]
            index_ -= 1

        nums[index_+1] = num_index

    return nums


if __name__ == '__main__':
    print(insert_sort(4))
