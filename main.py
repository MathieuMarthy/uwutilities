from uwutilities import Bar
import time

bar = Bar(300)

for _ in range(300):
    bar.next()
    time.sleep(1)
