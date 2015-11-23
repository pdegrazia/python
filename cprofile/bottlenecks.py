import cProfile
import time


def call1(a,b):

    time.sleep(.01)
    return a + b


def example(a,b):
    print call1(a,b)

if __name__ == '__main__':
    cProfile.run('example(1,2)')