from typing import List
from utils import fill_zeros, chunker, translate


def initializer(values: List[str]) -> List[List]:
    # convert from hex to python binary string (with cut bin indicator ('0b'))
    binaries = [bin(int(v, 16))[2:] for v in values]
    words = []
    for binary in binaries:
        word = []
        for b in binary:
            word.append(int(b))
        words.append(fill_zeros(word, 32, 'BE'))
    return words


def preprocess_message(message: str):
    """
    append a single ‘1’ to the end of the message
    determine the bit length of the message
    chunk it in a way that the total bit length is a multiple of 512
    :return: chunked bits
    """
    bits = translate(message)
    length = len(bits)
    message_len = [int(b) for b in bin(length)[2:].zfill(64)]
    bits.append(1)
    if length < 448:
        bits = fill_zeros(bits, 448, 'LE')
        bits = bits + message_len
        return [bits]
    elif 448 <= length <= 512:
        bits = fill_zeros(bits, 1024, 'LE')
        bits[-64:] = message_len
        return chunker(bits, 512)
    while (len(bits) + 64) % 512 != 0:
        bits.append(0)
    bits += message_len
    return chunker(bits, 512)

m = preprocess_message('hello world')
print(m)

