#!/usr/bin/python3
"""
Prime game module.
"""


def sieve_of_eratosthenes(n):
    """
    Generate a list of prime numbers up to n using
    the Sieve of Eratosthenes algorithm.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [num for num in range(2, n + 1) if primes[num]]


def is_prime(num):
    """
    Check if a given number is prime.
    """
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))


def game_winner(n):
    """
    Determine the winner of the prime game
    based on the number of primes up to n.
    """
    primes = sieve_of_eratosthenes(n)
    return "Ben" if len(primes) % 2 == 0 else "Maria"


def isWinner(x, nums):
    """
    Determine the overall winner of multiple rounds of the prime game.
    """
    winners = [game_winner(n) if is_prime(n) else "Ben" for n in nums]

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    return "Maria" if maria_wins > ben_wins else (
        "Ben" if ben_wins > maria_wins else None)
