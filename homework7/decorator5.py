def decorator_catch_exeptions(func):
    def decorated_func(*args, **kwargs):
        print('{} {}'.format('Enter', func.__name__))
        try:
            result = func(*args, **kwargs)
            print('{} {}'.format('Leave', func.__name__))
        except:
            print('{} {}'.format('Errors in', func.__name__))
            raise
        return result
    return decorated_func


@decorator_catch_exeptions
def test_5():
    print('Inside test_5')
    print(error)
    return 42

t = test_5()
print(t)

