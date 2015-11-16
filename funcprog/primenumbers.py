"""
my first example of functional programming

finding the prime numbers smaller than a given number n
"""
__author__ = 'paolo'


def has_dividends(n):
    dividers=filter(lambda x:n%x == 0,range(2,n))
    return dividers

def is_prime(n):
    if has_dividends(n):
        print 'number is not prime'
    else:
        print 'number is prime'

def main():
    is_prime(10)

if __name__ == '__main__':
    main()
