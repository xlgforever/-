# -*- coding: utf-8 -*-


def intToBin(spaces, i):
    '''
    spaces：字符长度
    i：十进制整数
    将十进制整数转换为指定长度的二进制表示
    '''
    return (bin(((1 << spaces) - 1) & i)[2:]).zfill(spaces)


def binToInt(spaces, s):
    '''
    spaces：字符长度
    s：0和1组成的二进制字符串
    将表示二进制的字符串转换为十进制数
    '''
    return int(s[1:], 2) - int(s[0]) * (1 << spaces - 1)


def convertBin(num, intLength, floatLength):
    '''
    num：需要转换的数
    intLength：整数位长度
    floatLength：小数位长度
    将小数转换为对应长度的0和1表示的二进制定点数字符串
    '''
    num_abs = abs(num)
    num_int = int(num_abs)
    num_float = num_abs - num_int

    num_int_bin = bin(num_int)[2:].zfill(intLength)

    float_to_int = round(num_float * ((1 << floatLength) - 1))
    num_float_bin = bin(float_to_int)[2:].zfill(floatLength)

    num_all = '0' + num_int_bin + num_float_bin
    if num < 0:
        num_all = list(num_all)
        for index, i in enumerate(num_all):
            if i == '1':
                num_all[index] = '0'
            else:
                num_all[index] = '1'
        num_all = ''.join(num_all)

        spaces = 1 + intLength + floatLength
        num_all = binToInt(spaces, num_all)
        num_all = num_all + 1
        num_all = intToBin(spaces, num_all)

    return num_all





