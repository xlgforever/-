# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:26:44 2019
对于得到诸如'0000010010011111'的字符串，如果使用内置的hex(int(data,2))函数就会把前
面的0自动忽略从而无法，即四个0无法被生成'0x0'，所以只能使用自定义函数.

在使用本方法得到结果result后，再使用bytes.fromhex(result)即可得到要发送的bytes数据
@author: fyan
"""
def bin_to_hex(string_bin):
    """
    每四位就进行一次转换，比如'0001'转换为'0x1'，然后去掉前两位，保留最后一位，最后
    将所有的最后一位拼接起来
    """
    length = len(string_bin)
    if (length % 4) != 0:
        return ValueError
    times = int(length/4)
    begin = 0
    end = 1
    hex_list = []
    while times > 0:
        tmp = string_bin[begin*4:end*4]
        begin += 1
        end += 1
        tmp = hex(int(tmp,2))[2:]
        hex_list.append(tmp)
        times -= 1
    return ''.join(hex_list)
    
    
