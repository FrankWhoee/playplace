from Crypto.Cipher import AES 
import os
import itertools

# from flag import FLAG

DATA = os.urandom(8)
DATA_2 = "a355c8b253a6f0037c9cd331c8b4b5afb7198c944e56db549612942ceec05e8c"

msg = "b8a363a95d83b3d13886dc97899844463d356fe030f67fa3681537a3d88e8966"

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
        # FIXME: i got this to work by putting a mod here, will ask the security team to review after the weekend
        # but we gotta get this live so ill just push it to prod
        # print(secret % 7 + 1)
        result = shuffle_using(result, secret % 7 + 1)
        # print("".join(result))
    key = "".join(result[:8])
    print(key)
    return bytes.fromhex(key)

def extend_key(key):
    return key * 8

def encrypt(key, message):
    key_one = key[:2]
    key_two = key[2:]
    
    key_one = extend_key(key_one)
    key_two = extend_key(key_two)

    c_one = AES.new(key_one, AES.MODE_ECB)
    c_two = AES.new(key_two, AES.MODE_ECB)

    return c_two.encrypt(c_one.encrypt(pad(message)))

def decrypt(key):
    key_one = key[:2]
    key_two = key[2:]

    key_one = extend_key(key_one)
    key_two = extend_key(key_two)

    c_one = AES.new(key_one, AES.MODE_ECB)
    c_two = AES.new(key_two, AES.MODE_ECB)
    # print(cipher.decrypt(bytearray.fromhex('b69dc7feb4888455859530b6009b33c7')))
    plaintext = c_two.decrypt(bytearray.fromhex(msg))
    plaintext = c_one.decrypt(plaintext)
    return plaintext

def bruteforce():
    sample = ['1','2','3','4','5','6','7']
    combs = ["".join(x) for x in list(itertools.product(sample,repeat=8))]
    i = 0
    for c in combs:
        i += 1
        if i % 1000 == 0:
            print("[{}/{}]".format(i,len(combs)))
        result = list(DATA_2)
        for secret in c:
            # FIXME: i got this to work by putting a mod here, will ask the security team to review after the weekend
            # but we gotta get this live so ill just push it to prod
            result = shuffle_using(result, int(secret))
        key = "".join(result[:8])
        plain = decrypt(bytearray.fromhex(key))
        if b'maple' in plain:
            print("DONE")
            print(plain)
            break
    # return bytes.fromhex(key)

# msg = encrypt(bytearray.fromhex('35823603'), b'FLAG').hex()

bruteforce()
# key = make_key()
# print(key)
# key = b'\xf6@\xa2\xb5'
# ct = encrypt(key, b'FLAG').hex()
# print(decrypt(key,ct))

# print("Decrypt this message to proceed: ", encrypt(key, b'FLAG').hex())
