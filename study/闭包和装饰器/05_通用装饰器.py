def decorator(func):

    def inner(*args,**kwargs):
        print("正在进行运算....")
        num = func(*args,**kwargs)
        return num

    return inner

@decorator
def fun_add(a,b):
    sum = a+b
    return sum

num = fun_add(1,2)
print(num)