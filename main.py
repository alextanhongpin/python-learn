from time import perf_counter as timer_func
import random
from contextlib import contextmanager


def common_item(seq1, seq2):
    """Find common items between two sequence"""
    common = []
    for item in seq1:
        if item in seq2:
            common.append(item)
    return common


@contextmanager
def timer():
    """A simple timing function for routines"""
    try:
        start = timer_func()
        yield
    except Exception as e:
        print(e)
        raise
    finally:
        end = timer_func()
        print('Time spent=>', 1000.0 * (end - start), 'ms.')


def test(n):
    """Generate test data for numerical lists given input size"""
    a1 = random.sample(range(0, 2 * n), n)
    a2 = random.sample(range(0, 2 * n), n)
    return a1, a2


with timer() as t:
    common = common_item(*test(100))
