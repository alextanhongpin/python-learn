#  $ pip3 install memory_profiler
# python3 -m memory_profiler memory_profiler.py


@profile
def squares(n):
    return [x * x for x in range(1, n + 1)]


squares(1000)
