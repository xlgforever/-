# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 09:05:06 2019
对于从开发板发送过来的bytes类型的数据，首先是使用convert_bytes函数将其转换为对应的
二进制字符串，然后使用本函数解析该字符串得到其表示的多个十进制数
本函数输入一串类似于'111100010001001'的数据，然后将其每一定的位数转换为对应的定点数
所表示的十进制数。
@author: fyan
"""
from bin_and_int import intToBin, binToInt


def sub_bin_to_dec(sub_string, fixed_point_number):
    """
    fixed_point_number：一个列表，其中有3个数字，依次表示：符号位位数、整数位位数、
        小数位位数
    sub_string：长度为sum(fixed_point_number)的二进制形式的字符串
    将某个长度的子字符串转换为一个十进制数
    """
    length = sum(fixed_point_number)
    if length != len(sub_string):
        return 'The length of sub_string is not match the fixed_point_number'
    
    abs_num = abs(binToInt(length, sub_string))
    abs_sub_string = intToBin(length, abs_num) # 将负数的二进制字符串转换为整数的二进制字符串，如果是整数，则不会引起变化
    
    pos_or_neg, int_length, float_length = fixed_point_number # 提取定点数的各个部分的位数
    int_sub_string = abs_sub_string[1:pos_or_neg+int_length] # 提取整数部分字符串
    float_sub_string = abs_sub_string[pos_or_neg+int_length:] # 提取小数部分字符串
    # 计算整数部分
    sub_int = int(int_sub_string,2)
    # 计算小数部分
    float_all = (1 << float_length) - 1 # 对应的二进制长度的最大值
    sub_float = int(float_sub_string, 2)/float_all #此处不能使用binToInt函数，因为这些字符串都不包含符号位
    
    sub_all = sub_int +sub_float
    if sub_string[0] == '0':
        return sub_all
    elif sub_string[0] == '1':
        return -sub_all
    
    
    
    
def bin_to_dec(string_bin, fixed_point_number):
    """
    string_bin：二进制形式的字符串
    fixed_poing_number：一个包含符号位位数、整数位位数和小数位位数的列表
    将一串二进制字符串中包含的多个十进制数按照给定的定点格式还原出来
    """
    single_length = sum(fixed_point_number)
    if (len(string_bin)%single_length != 0):
        return 'the length of string_bin is not match the fixed_point_number'
    
    begin = 0
    end = 1
    times = int(len(string_bin)/single_length)
    
    num_list = []
    while times > 0:
        tmp = string_bin[begin*single_length:end*single_length]
        tmp = sub_bin_to_dec(tmp, fixed_point_number)
        begin += 1
        end += 1
        times -= 1
        num_list.append(tmp)
    return num_list
    
    
