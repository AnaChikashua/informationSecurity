from typing import List


def translate(message: str) -> List[int]:
    char_codes = [ord(c) for c in message]
    _bytes = []
    for char in char_codes:
        _bytes.append(bin(char)[2:].zfill(8))
    bits = []
    for byte in _bytes:
        for bit in byte:
            bits.append(int(bit))
    return bits


def b2_to_b16(value: List[int]) -> hex:
    value = ''.join([str(x) for x in value])
    binaries = []
    for d in range(0, len(value), 4):
        binaries.append('0b' + value[d:d + 4])
    hexes = ''
    for b in binaries:
        hexes += hex(int(b, 2))[2:]
    return hexes


"""
In computing, endianness is the order or sequence of bytes of a word of digital data in computer memory. 
Endianness is primarily expressed as big-endian (BE) or little-endian (LE). 
A big-endian system stores the most significant byte of a word at the smallest memory address 
and the least significant byte at the largest. 
A little-endian system, in contrast, stores the least-significant byte at the smallest address.
"""


def fill_zeros(bits, length=8, endian='LE') -> List[bytes]:
    la = len(bits)
    if endian == 'LE':
        for i in range(la, length):
            bits.append(0)
    else:
        while la < length:
            bits.insert(0, 0)
            la = len(bits)
    return bits


def chunker(bits, chunk_length=8) -> List:
    chunked = []
    for b in range(0, len(bits), chunk_length):
        chunked.append(bits[b:b + chunk_length])
    return chunked


