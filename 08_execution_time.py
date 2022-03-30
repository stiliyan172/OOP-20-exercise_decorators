from time import time

def exec_time(func_ref):
    def wrapper(*args):
        # start stopwatch
        start = time()

        func_ref(*args)

        # stop stopwatch
        end = time()

        # return elapsed seconds
        return end - start
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1


print(loop())
