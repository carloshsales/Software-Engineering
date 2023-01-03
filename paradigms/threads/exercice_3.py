import threading
import time

def square(x, sec):
    print(f"SQUARE {x} waiting 3 sec...")
    time.sleep(sec)
    print(f"finish SQUARE {x ** 2}")

def cube(x, sec):
    print(f"CUBE {x} waiting 2 sec...")
    time.sleep(sec)
    print(f"finish CUBE {x ** 3}")

t1 = threading.Thread(target=square, args=(2, 3))
t2 = threading.Thread(target=cube, args=(2, 2))
t1.start()
t2.start()

t1.join()
t2.join()