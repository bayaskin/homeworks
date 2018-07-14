from functools import wraps

def decorator_logging_func(func):
    def decorated_func(*args, **kwargs):
        print ("{} {}".format('Enter', func.__name__))
        result = func(*args, **kwargs)
        print ('{} {}'.format('Leave', func.__name__))
        return result
    return decorated_func

@decorator_logging_func
def test_4():
    print("Inside test_4")
    return 42

t = test_4()

print(t)



