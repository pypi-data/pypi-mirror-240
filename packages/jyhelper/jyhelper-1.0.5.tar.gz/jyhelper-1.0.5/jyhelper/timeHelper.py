#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2020/12/16 16:07
# @Author : JY

import datetime
import time


class timeHelper:
    # 获取时间
    @staticmethod
    def getDate(timestamp=0, format_str='%Y-%m-%d %H:%M:%S'):
        if timestamp == 0:
            return datetime.datetime.now().strftime(format_str)  # 现在
        else:
            return datetime.datetime.fromtimestamp(timestamp).strftime(format_str)

    # 获取日期
    @staticmethod
    def getDay(timestamp=0, format_str='%Y-%m-%d'):
        if timestamp == 0:
            return datetime.datetime.now().strftime(format_str)  # 现在
        else:
            return datetime.datetime.fromtimestamp(timestamp).strftime(format_str)

    @staticmethod
    def getDayUTC(timestamp, format_str='%Y-%m-%d'):
        return datetime.datetime.fromtimestamp(timestamp - 8 * 3600).strftime(format_str)

    # 返回今天的日期
    @staticmethod
    def today(xcjt=0):
        return datetime.datetime.fromtimestamp(int(time.time()) + 86400 * xcjt).strftime('%Y-%m-%d')

    # 获取时间戳
    @staticmethod
    def getTime(date='', format_str=None):
        if date == '':
            return int(time.time())
        else:
            if format_str is None:
                if date.__len__() == 10:
                    format_str = '%Y-%m-%d'
                else:
                    format_str = '%Y-%m-%d %H:%M:%S'
            tm = time.strptime(date, format_str)
            return int(time.mktime(tm))

    @staticmethod
    def xcjt(small, big):
        big = big[:10] if big.__len__() != 10 else big
        small = small[:10] if small.__len__() != 10 else small
        format_str = '%Y-%m-%d'
        return int((int(time.mktime(time.strptime(big, format_str))) - int(
            time.mktime(time.strptime(small, format_str)))) / 86400 + 1)

    @staticmethod
    def getMonthFirstDay(day=None):
        day = day if day is not None else timeHelper.getDay()
        return day[:8] + '01'

    @staticmethod
    def getMonthEndDay(day=None):
        day = day if day is not None else timeHelper.getDay()
        year, month, tmp = day.split('-')
        if month == '12':
            nextMonth = 1
            year = str(int(year) + 1)
        else:
            nextMonth = int(month) + 1
        nextMonth = str(nextMonth) if nextMonth >= 10 else '0' + str(nextMonth)
        nextMonth = year + '-' + nextMonth + '-01'
        return timeHelper.getDay(timeHelper.getTime(nextMonth) - 86400)

    @staticmethod
    def addDay(event_day, add_day=1):
        return timeHelper.getDay(timeHelper.getTime(event_day) + 86400 * add_day)


if __name__ == '__main__':
    print(timeHelper.today(2))
    print(timeHelper.addDay(timeHelper.getDay(),1))
