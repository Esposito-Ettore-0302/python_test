from math import sqrt
from time import sleep
import threading, multiprocessing

def prime_thread():
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

def prime_process():
    thread_count = multiprocessing.cpu_count() * 4
    for I in range(thread_count):
        th = threading.Thread(target=prime_thread)
        th.start()
    block = input()

if __name__ == "__main__":
    processes_count = multiprocessing.cpu_count() * 4
    processes = []
    for i in range(processes_count):
        p = multiprocessing.Process(target=prime_process)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()