import math

from Crypto.Cipher import AES
import os
import itertools
# from flag import FLAG

DATA = os.urandom(8)
DATA_2 = "a355c8b253a6f0037c9cd331c8b4b5afb7198c944e56db549612942ceec05e8c"

# pads the message to a multiple of 16 bytes
def pad(msg):
    bytes_of_padding = (16 - len(msg)) % 16
    pad_bytes = bytes([bytes_of_padding]) # creates a single byte that has the numerical value of the number of bytes of padding you want
                                          # this padding scheme is called PKCS, don't worry about it, just know it pads the message to 16 bytes
    return msg + pad_bytes * bytes_of_padding

def shuffle_using(xs, y):
    for i in range(0, len(xs), y):
        xs.append(xs.pop(i))
    return xs

def make_key():
    result = list(DATA_2)
    for secret in DATA:
        # I got yelled at by the security team... they said I needed more bits
        result = shuffle_using(result, secret % 16 + 1)
    key = "".join(result[:8])
    return bytes.fromhex(key)

def extend_key(key):
    return key * 8

def encrypt(key, message):
    key_one = key[:2]
    key_two = key[2:]
    key_one = extend_key(key_one)
    key_two = extend_key(key_two)
    print(key_one)
    print(key_two)
    c_one = AES.new(key_one, AES.MODE_ECB)
    c_two = AES.new(key_two, AES.MODE_ECB)

    return c_two.encrypt(c_one.encrypt(pad(message)))

def decrypt(key, ciphertext):
    c = AES.new(key, AES.MODE_ECB)

    plaintext = c.decrypt(ciphertext)
    return plaintext

def halfEncrypt(key, message):
    c = AES.new(key, AES.MODE_ECB)

    ciphertext = c.encrypt(message)
    return ciphertext

import time

def bruteforce(knownmsg, knowncipher):
    t0 = time.time()
    tf = time.time()
    i = 0
    combs = math.comb(len(DATA_2),4)
    leftmap = {}
    rightmap = {}
    for c in itertools.combinations(DATA_2, r=4):
        i += 1
        if i % 1000:
            print("[{}/{}] {}% AVG: {}, EST: {}".format(i, combs, int((i/combs) * 100), str((tf - t0)/i)[0:4], int(((tf - t0)/i) * combs - (tf-t0))))
        key = bytearray.fromhex("".join(c))
        key = extend_key(key)

        leftmap[halfEncrypt(key, knownmsg)] = c
        rightmap[decrypt(key, bytearray.fromhex(knowncipher))] = c
        tf = time.time()
    print("DONE PRECOMPUTE-------------------------------------------------")
    i = 0
    t0 = time.time()
    tf = time.time()
    combs=len(leftmap)
    for k,v in leftmap.items():
        i += 1
        if i % 1000:
            print("[{}/{}] {}% AVG: {}, EST: {}".format(i, combs, int((i / combs) * 100), (tf - t0) / i,
                                                        int(((tf - t0) / i) * combs)))
        if k in rightmap:
            print("DONE--------------------------------")
            print(v)
            print(rightmap[k])
            break
        tf = time.time()


bruteforce(pad(b"is this thing on"), "3d23351bb8a61128ff846e5ea736cab2")

# key_one = "3a0c"
# key_two = "d3b5"
#
# key_one = extend_key(bytearray.fromhex(key_one))
# key_two = extend_key(bytearray.fromhex(key_two))
#
#
#
# cipher = "20a667175dfa51fc1ef0b4c73fc6c96ba29fbd7612015d389a3c35b753124822"
# cipher = bytearray.fromhex(cipher)
#
# plaintext = decrypt(key_two, cipher)
# plaintext = decrypt(key_one, plaintext)
print(plaintext)

#
# key = make_key()
# # print(key)
#
#
# key = b'\xc3\x1b[\x1e'
# key_one = b'\xc3\x1b\xc3\x1b\xc3\x1b\xc3\x1b\xc3\x1b\xc3\x1b\xc3\x1b\xc3\x1b'
# key_two = b'[\x1e[\x1e[\x1e[\x1e[\x1e[\x1e[\x1e[\x1e'
# lefttoright = pad(b"is this thing on")
#
# # print("Decrypt this message to proceed: ", encrypt(key, b"FLAG").hex())
# print(encrypt(key, lefttoright).hex())
#
#
#
# # c_one = AES.new(key_one, AES.MODE_ECB)
# #
# #
# # test = c_one.encrypt(pad(lefttoright))
# # print(test.hex())
# #
# # c_two = AES.new(key_two, AES.MODE_ECB)
# # print(c_two.encrypt(pad(test)).hex())
#
# print(lefttoright)
# lefttoright = halfEncrypt(key_one, lefttoright).hex()
# print(lefttoright)
# # lefttoright = halfEncrypt(key_two, bytearray.fromhex(lefttoright)).hex()
# # print(lefttoright)
#
# righttoleft = "bce0d400fd08fa57b6da4ceab5459cec"
# righttoleft = decrypt(key_two, bytearray.fromhex(righttoleft)).hex()
# print(righttoleft)
# righttoleft = decrypt(key_one, bytearray.fromhex(righttoleft))
# print(righttoleft)

#
# message = b"is this thing on"
# print("Intercepted test message: ", encrypt(key, message).hex())