from sha256 import sha256
import hashlib

m = hashlib.sha256()
m.update(b'hello world')
print(m.hexdigest())
print(sha256('hello world'))

# bit length: 0
hash_0 = sha256('')
vector_hash_0 = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
print('bit size 0: ', hash_0 == vector_hash_0)
# bit length: 24
hash_24 = sha256('abc')
vector_hash_24 = 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
print('bit size 24: ', hash_24 == vector_hash_24)
