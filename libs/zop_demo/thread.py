import threading
import time

def task(name):
    print(f"{name} started")
    #time.sleep(3)

    total = 0

    for i in range(100_000_000):
        total += i


    print(f"{name} finished")

t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))

t1.start()
t2.start()

t1.join()
t2.join()