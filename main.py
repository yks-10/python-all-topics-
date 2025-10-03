import multiprocessing as mp
import time
import os


def sample_worker(name):
    print('Worker {} started'.format(name))
    time.sleep(1)
    print('Worker {} finished'.format(name))



if __name__ == '__main__':
    p1 = mp.Process(target=sample_worker, args=('YOGESH',))
    p2 = mp.Process(target=sample_worker, args=('AJAY',))

    p1.start()
    p2.start()

    p1.join()
    p2.join()