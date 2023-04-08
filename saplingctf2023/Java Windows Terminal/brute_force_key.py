from collections.abc import Set

from Crypto.PublicKey import RSA
from Crypto.Util.number import getPrime, inverse, isPrime

actualpubkey = b'-----BEGIN PUBLIC KEY-----\nMIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQBfi4oFnOvmiBjXvDcwzpDv\nmsKnVXF4e30pk10RTVg+SRVRNcGRLQXVpygIHK1vRv//zLisno134ypkhgUQxznb\nzI9n5r1/x5QcYbO06M5FL4EPPXm90KWpDvBOmcdr/g/xZg/IzPqiYdQIvDlLE4F3\nAcng2JXGL4o2OHvj8yth6dKkjgAg/OKqKzLJ+szwiKyXFuBoUbxTEqsujj9rWVam\nCvTadG6xlX3AeX+Gxo818fj4FRmsuiduXuBurgMZs+4U+nqDG52PRyPs3IeCIt/6\nahLR8s9Q/mzs9s9Z8GE6s013BsPRvyw2yR/HHJWkRHqn0U2q1U4hHnWyWbJT53zl\nAgMBAAE=\n-----END PUBLIC KEY-----'
exppubkey = b''
usedprimes = set()

p = getPrime(1024)
while actualpubkey != exppubkey:
    print("Tried {} primes".format(len(usedprimes)))
    if p in usedprimes:
        continue
    q = p + 2
    while not isPrime(q):
        q += 2

    N = p * q
    e = 65537
    phi = (p-1) * (q-1)
    d = inverse(e, phi)

    key = RSA.construct((N, e, d, p, q))
    exppubkey = key.publickey().exportKey('PEM')
    usedprimes.add(p)
    p = getPrime(1024)


with open("private.key", 'wb') as content_file:
    content_file.write(key.exportKey('PEM'))

pubkey = key.publickey()

with open("public.key", 'wb') as content_file:
    content_file.write(pubkey.exportKey('PEM'))