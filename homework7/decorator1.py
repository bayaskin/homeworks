import datetime


def canceled_decorator(func):
    def cancel(*args, **kwargs):
        print ('{} {}'.format(str(func.__name__), "is canceled"))
        pass
    return cancel

@canceled_decorator
def test_1(self):
    return self

t = test_1
t(1)

