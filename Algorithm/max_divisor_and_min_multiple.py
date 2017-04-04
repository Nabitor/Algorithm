# -*- coding=utf-8 -*-


def get_max_divisor(m, n):
    """
    使用辗转相除法求最大公约数
    """
    if m < n:  # 保持n为最小值
        m, n = n, m

    r = 1
    while r:
        r = m % n
        m = n
        n = r

    return m


def get_min_multiple(m, n):
    """
    通过最大公约数求最小公倍数
    """
    max_divisor = get_max_divisor(m, n)

    return m*n//int(max_divisor)

if __name__ == '__main__':
    print(get_max_divisor(6, 2))
    print(get_min_multiple(3, 4))
