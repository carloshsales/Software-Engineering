import threading
import time

def wait(sec, thread_name):
    print(f"{thread_name} waiting {sec} sec...")
    time.sleep(sec)
    print(f"finish {thread_name}")


t1 = threading.Thread(target=wait, args=(3, "Thread 1"))
t2 = threading.Thread(target=wait, args=(2, "Thread 2"))
t1.start()
t2.start()

t1.join()
t2.join()