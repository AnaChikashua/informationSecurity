"""
These are merely utility functions and required the way they are because of using lists
instead of Python’s built-in binary representations.
"""


def is_true(x): return x == 1


def if_(i, y, z): return y if is_true(i) else z


def and_(i, j): return if_(i, j, 0)


def AND(i, j): return [and_(ia, ja) for ia, ja in zip(i, j)]


def not_(i): return if_(i, 0, 1)


def NOT(i): return [not_(x) for x in i]


# return true if either i or j is true but not both at the same time
def xor(i, j): return if_(i, not_(j), j)


def XOR(i, j): return [xor(ia, ja) for ia, ja in zip(i, j)]


# if number of truth values is odd then return true
def xor_xor(i, j, l): return xor(i, xor(j, l))


def XORXOR(i, j, l): return [xor_xor(ia, ja, la) for ia, ja, la in zip(i, j, l)]


# get the majority of results, i.e., if 2 or more of three values are the same
def maj(i, j, k): return max([i, j, ], key=[i, j, k].count)

