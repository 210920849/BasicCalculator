from time import strftime


def now():
    """返回系统当前时间的字符串，格式为：年月日时分秒"""
    return strftime("%Y%m%d%H%M%S")



if __name__ == '__main__':
    print(now())
