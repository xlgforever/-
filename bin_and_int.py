# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 09:52:26 2019

@author: fyan
"""

def intToBin(spaces, i):
    '''
    spaces：字符长度
    i：十进制整数
    将十进制整数转换为指定长度的带符号位的二进制表示
    '''
    return (bin(((1 << spaces) - 1) & i)[2:]).zfill(spaces)


def binToInt(spaces, s):
    '''
    spaces：字符长度
    s：0和1组成的二进制字符串
    将表示二进制的带符号位的字符串转换为十进制数
    '''
    return int(s[1:], 2) - int(s[0]) * (1 << spaces - 1)