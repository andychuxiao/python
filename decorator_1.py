def decorator(func):
    print("hello")
    return func

@decorator
def foo():
    print("foo name = %s"%foo.__name__)

foo()