def decorator_with_params(arg_of_decorator):#这里是装饰器的参数
    print(arg_of_decorator) 
    def newDecorator(func):#最终被返回的函数
        print(func) 
        return func
    return newDecorator


@decorator_with_params("deco_args")
def foo3():
    print("foo3 name = %s"%foo3.__name__)
foo3()