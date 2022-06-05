from gates import xor_xor, maj


def rot_r(x, n): return x[-n:] + x[:-n]


def sh_r(x, n): return n * [0] + x[:-n]


def add(i, j):
    if len(i) != len(j):
        print('Length are different!')
        return None
    length = len(i)
    sums = list(range(length))
    c = 0
    for x in range(length - 1, -1, -1):
        sums[x] = xor_xor(i[x], j[x], c)
        c = maj(i[x], j[x], c)
    return sums


