from multiprocessing import Pool
import time
def countdown(n):
    while n > 0:
        n -= 1
    return n
COUNT = 10000000
start = time.time()

if __name__ == '__main__':
    with Pool() as p:
        p.map(countdown, [COUNT/2, COUNT/2])
end = time.time()
print(end-start)