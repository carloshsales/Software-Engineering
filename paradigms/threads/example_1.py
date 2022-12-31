# import threading
# from time import sleep

# def wait():
#     sleep(0.5)
#     print("Esperou")

# t = threading.Thread(target=wait, name="")
# t.start()

# print(t.is_alive())
# sleep(1)
# print(t.is_alive())

import threading
from time import sleep

def wait():
    count = 0
    print(count)
    count += 1
    sleep(0.1)

t = threading.Thread(target=wait, name="Wait", daemon=True)#daemon kill thread in process end
t.start()

print(t.is_alive())
sleep(1)
print(t.is_alive())
