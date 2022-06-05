from init_constants import K, H
from preprocess import initializer, preprocess_message, chunker
from gates import XORXOR, XOR, AND, NOT
from operations import rot_r, sh_r, add
from utils import b2_to_b16


def sha256(message):
    k = initializer(K)
    h0, h1, h2, h3, h4, h5, h6, h7 = initializer(H)
    chunks = preprocess_message(message)
    for chunk in chunks:
        w = chunker(chunk, 32)
        for _ in range(48):
            w.append(32 * [0])
        for i in range(16, 64):
            s0 = XORXOR(rot_r(w[i - 15], 7), rot_r(w[i - 15], 18), sh_r(w[i - 15], 3))
            s1 = XORXOR(rot_r(w[i - 2], 17), rot_r(w[i - 2], 19), sh_r(w[i - 2], 10))
            w[i] = add(add(add(w[i - 16], s0), w[i - 7]), s1)
        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7
        for j in range(64):
            S1 = XORXOR(rot_r(e, 6), rot_r(e, 11), rot_r(e, 25))
            ch = XOR(AND(e, f), AND(NOT(e), g))
            temp1 = add(add(add(add(h, S1), ch), k[j]), w[j])
            S0 = XORXOR(rot_r(a, 2), rot_r(a, 13), rot_r(a, 22))
            m = XORXOR(AND(a, b), AND(a, c), AND(b, c))
            temp2 = add(S0, m)
            h = g
            g = f
            f = e
            e = add(d, temp1)
            d = c
            c = b
            b = a
            a = add(temp1, temp2)
        h0, h1, h2, h3, h4, h5, h6, h7 = add(h0, a), add(h1, b), add(h2, c), add(h3, d), add(h4, e), add(h5, f), add(h6,g), add(h7, h)
        digest = ''
        for val in [h0, h1, h2, h3, h4, h5, h6, h7]:
            digest += b2_to_b16(val)
        return digest
