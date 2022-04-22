#多个装饰器的执行过程：就近原则

#在进行div标签的装饰
def make_div(func):
    def inner():
        result = "<div>"+func()+"</div>"
        return result
    return inner

#先进行p标签的装饰
def make_p(func):
    def inner():
        result = "<p>"+func()+"</p>"
        return result
    return inner

@make_div
@make_p
def content():
    return "人生苦短，我用python！"

result = content()
print(result)
