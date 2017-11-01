
def decorator_func_args(func):
    def handle_args(*args,**kw): #处理传入函数的参数
        print("begin")
        func(*args,**kw)   #函数调用
        print("end")
    return handle_args


@decorator_func_args
def foo2(a,b=2):
    print(a,b)
    print("foo2 name = %s"%foo2.__name__)

foo2(1)