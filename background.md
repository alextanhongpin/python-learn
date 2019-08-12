## Running a background task as daemon

```python
from datetime import datetime
import time
import threading

class TestThreading:
    def __init__(self, interval=1):
        self.interval = interval
        self.running = True
        
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()
    
    def run(self):
        while self.running:
            print(datetime.now().__str__() + ': Start task in the background')
            time.sleep(self.interval)

tr = TestThreading()
time.sleep(1)
print('hello world')
time.sleep(2)
print('this is good')
tr.running = False
```
