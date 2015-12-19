'''
This module calculates the smallest prime before a given number
or the largest prime after the given number
'''

import cProfile

class Prime:

    def __init__(self,number):
        self.number=number
        self.primes = self._generator()

    def _generator(self):
        primes_list=[]
        for num in range(2,self.number):
            if not self.__is_prime(num):
                primes_list.append(num)

        return primes_list

    def __is_prime(self, number):
        return filter(lambda x: number % x == 0, range(2,number))

    def print_all_primes(self):
        for prime in self.primes:
            print prime

    def print_bigger_prime_before(self):
        print self.primes[-1]

if __name__ == '__main__':
    cProfile.run('number = Prime(1000)')

    cProfile.run('number.print_all_primes()')

    cProfile.run('number.print_bigger_prime_before()')
