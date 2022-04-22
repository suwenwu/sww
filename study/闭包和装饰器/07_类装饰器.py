class MyDecoritor(object):
    def __init__(self,func):
        #将func私有化
        self.__func = func
    
    #__call__方法使类实例化之后可以加小括号
    def __call__(self, *args, **kwds):
        print("先登陆才可以发表评论")
        self.__func()

@MyDecoritor
def comment():
    print("发表评论")

comment()