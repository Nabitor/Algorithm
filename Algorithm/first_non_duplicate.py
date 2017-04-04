# -*- coding=utf-8 -*-


def get_first_non_duplicate_value(array):
    if not isinstance(array, list):
        print("数据格式有误，请重新输入。")
        return

    first_happen = [i for i in range(9)]
    re_happen = [i for i in range(9)]

    for item in array:
        item_ascii = ord(str(item))  # 获取对应的ascii码

        if first_happen[item_ascii // 32] & (1 << (item_ascii % 32)) == 0:
            first_happen[item_ascii // 32] = first_happen[item_ascii // 32] | \
                                             (1 << (item_ascii % 32))
        else:
            re_happen[item_ascii // 32] = re_happen[item_ascii // 32] | \
                                        (1 << (item_ascii % 32))

    index = 0
    for i, item in enumerate(array):
        item_ascii = ord(str(item))

        if re_happen[item_ascii // 32] == re_happen[item_ascii // 32] | \
                (1 << (item_ascii % 32)) == 0:
            index = i
            break

    print(first_happen)
    print(re_happen)
    print(index)


if __name__ == '__main__':
    get_first_non_duplicate_value([1, 2, 3, 1])
