import threading
import time


def async_task(duration=1):
    time.sleep(1)
    print('done')


for i in range(0, 5):
    t = threading.Thread(target=async_task, args=(1, ))
    t.start()
