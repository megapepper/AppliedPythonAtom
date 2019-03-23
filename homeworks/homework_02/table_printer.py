#!/usr/bin/env python


def tabulate(list_of_entries):
    l_of_cols = []
    hs = []
    if list_of_entries is None:
        raise ValueError
    column_count = len(list_of_entries)
    line_count = len(list_of_entries[0])
    if column_count == 0:
        raise ValueError
    if line_count < 1:
        raise ValueError
    for i in range(0, column_count):
        l_of_cols.append(0)
        if len(list_of_entries[i]) < 1:
            raise ValueError
        for k in range(0, len(list_of_entries[i])):
            if k == 0:
                hs.append(str(list_of_entries[i][k]))
            if len(str(list_of_entries[i][k])) > l_of_cols[i]:
                l_of_cols[i] = len(str(list_of_entries[i][k]))
    str_zero = '|'
    for i in range(0, len(hs)):
        s = 2 if l_of_cols[i] % 2 == 1 else 1
        tempstr = ' ' * (l_of_cols[i] // 2 + 2 - len(hs[i]) // 2) + hs[i]
        str_zero += tempstr
        str_zero += ' ' * (l_of_cols[i] + 4 - len(tempstr)) + '|'
    print('-' * len(str_zero))
    print(str_zero)
    line = 1
    for k in range(1, line_count):
        for i in range(0, column_count):
            try:
                s = str(list_of_entries[i][k])
            except IndexError:
                break
            if not s:
                raise ValueError
            try:
                float(s)
            except ValueError:
                print('|' + ' ' * 2 + s + (l_of_cols[i] - len(s) + 2) *
                      ' ', end='')
                continue
            print('|' + ' ' * (l_of_cols[i] - len(s) + 2) + s + 2 *
                  ' ', end='')
        print("|\n", end='')
    print('-' * len(str_zero))
