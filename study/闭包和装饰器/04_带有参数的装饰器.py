#return_decoretor函数返回的是一个装饰器
def return_decoretor(flag):
    #装饰器有且只能有一个参数，也就是函数
    def decoretor(func):
        def inner(a,b):
            if flag == '+':
                print("正在努力进行加法运算")
            else:
                print("正在努力进行减法运算")
            result = func(a,b)
            return result
        return inner
    return decoretor

@return_decoretor("+")
def add_num(a,b):
    return a+b;

result = add_num(1,2)
print(result)