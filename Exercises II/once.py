
def once(fn):
    fn.called = False
    def inner(*args):
        if fn.called == False:
            fn.called = True
            return fn(*args)
        return None
    return inner




"""
# Course solution:

def once(fn):
    fn.is_called = False
    def inner(*args):
        if not(fn.is_called):
            fn.is_called = True
            return fn(*args)
    return inner
"""


def add(a,b):
    return a+b






oneAddition = once(add)

print(oneAddition(2,2)) # 4
print(oneAddition(2,2)) # None
print(oneAddition(12,200)) # None