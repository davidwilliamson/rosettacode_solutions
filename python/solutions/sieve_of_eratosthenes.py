#! /usr/bin/env python

"""Sieve of Eratosthenes

https://rosettacode.org/wiki/Sieve_of_Eratosthenes

Implement the Sieve of Eratosthenes algorithm, with the only allowed optimization
that the outer loop can stop at the square root of the limit, and the inner loop
may start at the square of the prime just found.

"""

import math


def main():
    """main"""
    upper_limit = 53
    candidate_primes = {num: True for num in range(2, upper_limit+1)}
    for candidate in range(2, int(math.sqrt(upper_limit) + 1.0)):
        if candidate_primes[candidate]:
            for multiple in range(candidate*candidate, upper_limit+1, candidate):
                candidate_primes[multiple] = False
    print("primes: up to {0}:\n{1}".format(
        upper_limit,
        ", ".join([str(p) for p in candidate_primes if candidate_primes[p]])))


if __name__ == '__main__':
    main()
