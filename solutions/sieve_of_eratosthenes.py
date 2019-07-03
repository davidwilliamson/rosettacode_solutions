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
    upper_limit = 50
    candidate_primes = {num: True for num in range(2, upper_limit+1)}
    for candidate in range(2, int(math.sqrt(upper_limit))):
        if candidate_primes[candidate]:
            c_sqr = candidate*candidate
            # n^2+0n, n^2+1n, n^2+2n ...
            multiples = [
                c_sqr + candidate*multiple for multiple
                in range(0, int((upper_limit - c_sqr)/candidate)+1)
            ]
            # print("multiples of {0}: {1}".format(candidate, multiples))
            for multiple in multiples:
                candidate_primes[multiple] = False
    print("primes: up to {0}:\n{1}".format(
        upper_limit,
        ", ".join([str(p) for p in candidate_primes if candidate_primes[p]])))


if __name__ == '__main__':
    main()
