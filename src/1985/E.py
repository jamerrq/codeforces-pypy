import sys
from functools import reduce


"""
--
    Problem name: E. Secret Box
    Link: https://codeforces.com/contest/1984/problem/E
    Site: Codeforces
    Contest: Codeforces Round 952 (Div. 4)
    Status: AC
--
"""


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


def binary_search(arr, x):
    """
    return the latest position in arr such that the element at this index
    is lower or equal to the x value
    if no such element exists, it returns -1

    Args:
        arr (list): sorted list to search on
        x (int): value to compare the elements

    Returns:
        int: index of latest element lower or equal to x
    """
    i, j = 0, len(arr) - 1
    ans = -1
    #
    while i <= j:

        mid = i + (j - i) // 2
        xmd = arr[mid]

        if xmd <= x:
            ans = mid
            i = mid + 1

        else:
            j = mid - 1

    return ans


def gcd(a, b):
    """
    Greatest common divisor algorithm
    https://cp-algorithms.com/algebra/euclid-algorithm.html

    Args:
        a (int): number 1
        b (int): number 2

    Returns:
        int: gcd of a and b
    """
    if not b:
        return a

    return gcd(b, a % b)


def lcm(a, b):
    """
    Least common multiple

    Args:
        a (int): number 1
        b (int): number 2

    Returns:
        int: lcm of a and b
    """
    return a / gcd(a, b) * b

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def solve():
    x, y, z, k = read_array()
    #
    ans = 0
    #
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if k % (i * j):
                continue
            #
            tmp = k // (i * j)
            if tmp > z:
                continue
            #
            curr = (x - i + 1) * (y - j + 1) * (z - tmp + 1)
            ans = max(ans, curr)
    #
    print(ans)


t = read()
for _ in range(t):
    solve()
