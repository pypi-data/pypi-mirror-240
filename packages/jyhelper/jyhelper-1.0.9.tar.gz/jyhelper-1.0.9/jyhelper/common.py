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
        if not isinstance(delValues,list):
            delValues = [delValues]
        for delValue in delValues:
            needList = [x for x in needList if x != delValue]
        return needList


if __name__ == '__main__':
    test = ['a','b','a','c','d',None]
    print(common.delListValue(test,['f',None,'a']))
    print(test)
