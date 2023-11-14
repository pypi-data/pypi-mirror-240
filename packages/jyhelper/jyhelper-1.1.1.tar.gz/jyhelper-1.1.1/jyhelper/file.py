#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2023/11/14 14:03 
# @Author : JY
"""
文件操作相关
"""


class file(object):
    def __init__(self):
        pass

    # 一次性读取txt文件的全部内容
    @staticmethod
    def readTxtFile(filePath,encoding='utf-8'):
        with open(filePath,'r',encoding=encoding) as f:
            content = f.read()
        return content

    # 以追加的形式写文件
    @staticmethod
    def writeTxtFileAppendMode(filePath,content,encoding='utf-8'):
        with open(filePath, 'a', encoding=encoding) as f:
            f.write(content)

    # 清空文件后写入
    @staticmethod
    def writeTxtFileNewMode(filePath,content,encoding='utf-8'):
        with open(filePath, 'w', encoding=encoding) as f:
            f.write(content)


if __name__ == '__main__':
    file()
