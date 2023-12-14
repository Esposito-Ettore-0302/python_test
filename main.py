from math import sqrt
from time import sleep
import threading, multiprocessing

def primeS():
    n = 0
    while True:
        n += 1
        prime = True
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            print(n)

processes = multiprocessing.cpu_count() * 4
for i in range(processes):
    p = threading.Thread(target=primeS)
    p.start()
block = input()