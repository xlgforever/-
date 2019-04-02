# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 14:31:58 2018

@author: fyan
"""

def convert_bytes(s):
    '''
    将输入的bytes类型变量s转换为二进制字符串
    '''
    str1 = []
    for i in s:
        i = bin(int(str(i),10))[2:]
        i = str(i)
        i = i.zfill(8)
        str1.append(i)
        
    return ''.join(str1)

if __name__ == '__main__':
   a = convert_bytes(read_data)