#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-09 18:51:28
# @Author  : xuejun (xj174850@163.com)
# @Link    : https://github.com/NeuObito
# @Version : 0.1
import os


def get_parent(i):
    return (int(i) >> 1) - 1


def get_left(i):
    return i << 1


def get_right(i):
    return (i << 1) + 1


def heapify(l, i):
    n = len(l)
    left = get_left(i)
    right = get_right(i)
    smallest = i

    if left < n and l[left] < l[i]:
        smallest = left

    if right < n and l[right] < l[smallest]:
        smallest = right

    if smallest != i:
        l[i], l[smallest] = l[smallest], l[i]
        i = smallest
    else:
        return


if __name__ == '__main__':
    print(os.path.basename(__file__))
    _l = [1, 3, 5, 2, 8, 9, 4]
    heapify(_l, 0)
    print(_l)
