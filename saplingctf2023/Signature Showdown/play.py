import math
from sympy.ntheory import discrete_log
from Crypto.Util.number import getPrime, bytes_to_long, inverse, long_to_bytes
#
# def verify(sig, msg):
#     return msg == long_to_bytes(pow(bytes_to_long(sig), e, N))
#
#
# def sign(msg):
#     return long_to_bytes(pow(bytes_to_long(msg), d, N))
#
# p = getPrime(512)
# q = getPrime(512)
# N = p * q
# e = 65537
#
# print("N:", hex(N))
#
# phi = (p - 1) * (q - 1)
# d = inverse(e, phi)
#
# N = 0x9737e6331944e5c54ba917264071d4250fea546434705cf7ab81e2cf8012ec5619b490a1653a40b78528eed926fe48af8fea94d772bd944b7a8f6ba54416d061de1651fea158e45778d1d3d86818b1fbf3ba5bfdaa94a786dc9c35437c309d95f25f19b0358b3396abe15f44f4c54f21a20e1c796cf17c0eeb5ca8048bfed467
# e = 65537
# msg1 = b"Baba is you."
# sig1 = 0x521e95e2928c496b49fcfe039b1b9296d51d4b7970a2569ab16187783e5739b22fcc44e1e9d9f1f74e8aadd5abf55acd5e4b8c4949747a8107398f35709bfb9e01ad2dc1a7c15f7a82ff2be666e74fca3c030aae378583a3a45c5b9ef88e83d68aa21c37c759721f71db361b7c87eb38196994ad1464ddf28d12dc5c8900f100
# msg2 = bytes.fromhex('baba')
# sig2 = 0x5b478d4d12e5d9e5f62bb9f028336ac8ccd90e4d76a9f73fa41a52cbbab88463140fce83e3e40cb557a91ea82d27aef2806fa79a4ac39e9fd3dd5fa6ff45a24a96bed5cfcd1be7bfd4da6a918ccb13923a27bee696f408fa472fac835ab421fd71dd2a1b5a2765ad53e07fd7b7a0f341387f6175dbc03eb3805a91c5be8b7396
# msg3 = b"Baba is flag."
# sig3 = sign(msg3)
# print(sig3)
# y = 1
# while pow(2885428159,y,2246884751) != 1861653051:
#     print(y)
#     y += 1
# print("DONE: {}".format(y))
print("f" * 140 + "55baa500")