import datetime

def timeit(func):
    def check_time(*args, **kwargs):
        before = datetime.datetime.now()
        x = func(*args, **kwargs)
        after = datetime.datetime.now()
        print("Speed = {0}".format(after-before))
        return x
    return check_time

@timeit
# class Foo():
def test_2(self):
    print("In")
    import time
    time.sleep(5)
    print("Out")

t = test_2

t(1)
