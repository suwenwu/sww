# 1.函数嵌套
def config_name(name):
    def inner(msg):
        # 2.内部函数使用外部函数变量
        print(name + "说:" + msg)

    # 返回内部函数名
    return inner


# 创建闭包实例
tom = config_name("tom")
jerry = config_name("jerry")
tom("哥们，过来一起玩耍啊")
jerry("打死都不去")
