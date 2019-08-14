## Rate limiting with Python

```python
import time
import threading


class LeakyBucket:
    def __init__(self, rps):
        self.rps = rps
        self.next_allowed_time = time.time()

    def allow(self):
        now = time.time()
        if now >= self.next_allowed_time:
            self.next_allowed_time += 1 / self.rps
            return True
        return False


leakyBucket = LeakyBucket(1)
print(leakyBucket.allow())
print(leakyBucket.allow())
print(leakyBucket.allow())
time.sleep(1)
print(leakyBucket.allow())
print(leakyBucket.allow())


class TokenBucket:
    def __init__(self, rps):
        self.rps = rps
        self.counter = rps
        self.thread = threading.Thread(target=self.refill, args=())
        self.thread.daemon = True
        self.thread.start()

    def allow(self):
        if self.counter == 0:
            return False
        self.counter -= 1
        return self.counter < self.rps

    def refill(self):
        print('refill started')
        while True:
            time.sleep(1 / self.rps)
            if self.counter <= self.rps:
                print('refilling')
                self.counter += 1


token_bucket = TokenBucket(1)
print(token_bucket.allow())
print(token_bucket.allow())
time.sleep(1)
print(token_bucket.allow())
print(token_bucket.allow())
```
