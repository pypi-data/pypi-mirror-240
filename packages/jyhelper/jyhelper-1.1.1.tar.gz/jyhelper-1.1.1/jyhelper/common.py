from jyhelper import timeHelper


class common:

    # 打印日志
    @staticmethod
    def debug(*args, path=None):
        path = './debug.log' if path is None else path
        with open(path, 'a', encoding='utf-8') as f:
            f.write("\n---------------" + timeHelper.getDate() + "---------------\n")
            for arg in args:
                f.write(str(arg) + "\n")

    # 带时间输出
    @staticmethod
    def print(*args):
        print(timeHelper.getDate(), '--->', *args)

    # 将列表分割 每一份n的长度
    @staticmethod
    def explodeList(data, n):
        if isinstance(data, list):
            return [data[i:i + n] for i in range(0, len(data), n)]
        else:
            return []

    # 把英文的引号转换程中文的引号
    @staticmethod
    def replaceYinHao(strings):
        return strings.replace('"', '“').replace("'", "‘")

    # 把值转为int
    @staticmethod
    def transInt(val, default=0):
        try:
            val = int(val)
        except ValueError:
            val = default
        return val

    @staticmethod
    def transFloat(val, default=0):
        try:
            val = float(val)
        except ValueError:
            val = default
        return val

    # 从list中删除数据
    @staticmethod
    def delListValue(needList, delValues):
        if not isinstance(delValues, list):
            delValues = [delValues]
        for delValue in delValues:
            needList = [x for x in needList if x != delValue]
        return needList

    # 排序字典的key
    @staticmethod
    def sortDictByKey(my_dict, reverse=False):
        return dict(sorted(my_dict.items(), key=lambda x: x[0], reverse=reverse))

    # 排序字典的value
    @staticmethod
    def sortDictByValue(my_dict, reverse=False):
        return dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=reverse))


if __name__ == '__main__':
    # test = ['a','b','a','c','d',None]
    # print(common.delListValue(test,['f',None,'a']))
    # print(test)
    print(common.sortDictByKey({'c_actual收入': 900.0, 'a日期': '2023-11-09', 'b新增': 62, 'd留存1': 62, 'e收入1': 0, 'f付费人数1': 0, 'd留存2': 0, 'e收入2': 0, 'f付费人数2': 0, 'd留存3': 0, 'e收入3': 0, 'f付费人数3': 0}))
