# 装饰器特点：
# 1.不改变原有函数的写法
# 2.不改变原有函数的调用方式
# 3.给原有函数增加额外功能

def check(func):  # func就是要装饰的函数comment
    def inner():
        print("已经进行登陆验证")
        '''执行函数之前'''
        func()  # 调用comment
        '''执行函数之后'''
        print("评论好多啊")

    return inner


# 装饰器第二种写法：语法糖写法
@check
def comment():
    print("发表评论")


# 装饰器第一种写法
# comment = check(comment)

comment()
