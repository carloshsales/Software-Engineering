
import threading
import time

def wait(seconds, message):
    print(f"Start task {message}")
    time.sleep(seconds)
    print(f"End task {message}")

t = threading.Thread(name="wait", target=wait, args=(2, "Wait"))
t.start()
print("...")
t.join()
for i in range(3): 
    time.sleep(2)
    print(i)
print("Thread finished")