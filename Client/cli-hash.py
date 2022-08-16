#!/usr/bin/env python3

import sys
from Crypt.HMAC import HMAC
from Crypt.AES import AES
from Crypt.hash import HASH
from Crypt.SCrypt import SCRYPT


command = sys.argv[1]


def prf(key, msg):
    return HMAC(key=key, msg=msg, digestmod=HASH).digest()


if command == "help":
    print(f"using {sys.argv[0]}")
    print(
        f"{sys.argv[0]} aes encrypt|decrypt <stretched_master_key> <password_to_hash> <16_byte_init_vec>"
    )
    print(f"{sys.argv[0]} scrypt <password> <salt>")
elif command == "aes":
    if sys.argv[2] == "encrypt":
        print(AES(sys.argv[3]).encrypt_cbc(sys.argv[4], sys.argv[4]))
    elif sys.argv[2] == "decrypt":
        print(AES(sys.argv[3]).decrypt_cbc(sys.argv[4], sys.argv[5]))
    else:
        print("what the ****!!")
elif command == "scrypt":
    print(
        SCRYPT(
            password=sys.argv[2],
            salt=sys.argv[3],
            N=1_024,
            r=4,
            p=1,
            dkLen=128,
            prf=prf,
        ).scrypt()
    )
else:
    print("What the ****!!")
