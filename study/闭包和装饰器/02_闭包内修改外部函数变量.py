def fun_out():
    num1 = 10

    def fun_inner():
        # nonlocal关键字修改闭包函数变量
        nonlocal num1
        num1 = 20
        result = num1 + 10
        print(result)

    print("修改前num1的值为", num1)
    fun_inner()
    print("修改前后num1的值为", num1)
    return fun_inner


new_func = fun_out()
new_func()
