
from time import time

def timed(func):
    def wrapper(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('elapsed', after - before)
        return rv
    return wrapper        

@timed
def add(x, y = 10):
    return x + y

print(add(6,88)) 
print(add(7)) 
print(add(8)) 

