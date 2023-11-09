class common:

    # 将列表分割 每一份n的长度
    @staticmethod
    def explodeList(data, n):
        if isinstance(data, list):
            return [data[i:i + n] for i in range(0, len(data), n)]
        else:
            return []


if __name__ == '__main__':
    pass
