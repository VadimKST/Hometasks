import threading
import random
from time import sleep

forks = [threading.Lock() for i in range(5)]

philosophers = {
    0: (forks[0], forks[1]),
    1: (forks[1], forks[2]),
    2: (forks[2], forks[3]),
    3: (forks[3], forks[4]),
    4: (forks[4], forks[0])
}


def eating(i):
    left_fork = philosophers[i][0]
    right_fork = philosophers[i][1]

    while True:
        left_fork.acquire()
        if not right_fork.acquire(False):
            left_fork.release()
            left_fork, right_fork = right_fork, left_fork
        else:
            break

    print(f'Eating {threading.current_thread().name}')
    sleep(random.randint(1, 2))
    print(f'Finished {threading.current_thread().name}')
    philosophers[i][0].release()
    philosophers[i][1].release()


while True:
    i = random.randint(0, 4)
    th = threading.Thread(target=eating, name=f'philosopher {i}', args=(i,))
    th.start()
