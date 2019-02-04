# pip3 install line_profiler

# $ kernprof -l -v line_profiler.py


@profile
def is_prime(self):
    """Whether current value is prime"""
    vroot = int(self.value**0.5) + 1
    for i in range(3, vroot, 2):
        if self.value % i == 0:
            return False
    return True


if __name__ == "__main__":
    l = list(Prime(1000))
