#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-02
# @Author  : xuejun (xj174850@163.com)
# @Link    : https://github.com/NeuObito


def insert_sort(nums):
    '''
    最简单的插入排序，时间复杂度为O(n**2)
    '''
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


def binary_search(a, x, lo=0, hi=None):
    '''
    二分查找，找到插入排序元素应该插入的位置
    '''
    if lo < 0:
        raise ValueError("lo must be non-negative")

    if hi is None:
        hi = len(a)

    while lo < hi:
        mid = (lo + hi) // 2

        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1

    return mid


def insert_sort_user_binarysearch(nums):
    '''
    这一改进并没有提高插入排序的复杂度，仍然是O(n**2)
    只是比较次数减少了，为O(nlogn)
    '''
    if not isinstance(nums, list):
        return

    num_len = len(nums)
    if num_len <= 1:
        return nums

    for index in range(1, num_len):
        num_index = nums[index]
        p = binary_search(nums[:index], num_index)

        # 找到排序点从右遍历，可以减少遍历次数
        for j in range(index, p, -1):
            nums[j] = nums[j-1]

        nums[p] = num_index

    return nums


if __name__ == '__main__':
    print(insert_sort_user_binarysearch([4, 3, 2, 1]))
