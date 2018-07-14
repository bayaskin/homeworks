def decorator_count_calls(func):
    def _counting(*args, **kwargs):
        _counting.calls += 1
        return func(*args, **kwargs)
    _counting.calls = 0
    return _counting

@decorator_count_calls
def print_me(self):
    return self

test_3 = print_me
test_3(1)
test_3(2)
test_3(3)
test_3(4)
print (test_3.calls)



