##### ID = TeamBuffet, MASTER_PASSWORD = WeAre#1 #####

# Imports
from SCrypt import SCRYPT
from hash import HASH
from HMAC import HMAC
from HKDF import HKDF
from AES import AES

####################### GET PASSWORD #############################

# Database
stored_salt = b',W(:qErnEvZL)ywNW9%D-"Y_mQ9aGh:H*ummrRqbo717mO7LHzfBPzwSH=vT#T$'
auth = b'T_)\x86\xef\x13\x89\xb2|\x1a\x1bF\x1c0\x9d\xaf\xc5\xf0\xe5\x16\x02\xd9\n\x1fy\xf6\x10\xec\x06\xf4_.~~\x0f\xd5\xaaV\x1e\xb5q\x14\xcaJ\xe5\xee\xab\xbaX\xa8\xb3\xfc9\x18\x9b\xc5C\x8clp\xdc>\x8b\x9b\x06\xcbH\xd3?\xa5)\xac\xe0\x129\x19a\x99\xcc\\\x90F\xfd2\x81\xd3aP\x81\xeb\x017\xbf\x92\xe6r\xb9A\x83\xa4\x7f\xa6\xd2\x19\xfbTk\xfdR\xb6\xffk\xb5\xc1\xda\xd9\xe9\x94\xb2 \xe1\x0c\x17\xd8\x81\x9e\xcc\x17'
protected_key = b'\xfc\tu\x1f\xc9\xe5m\x07k*|\xebT\x19\xea\xbd'
init_vec = b'kK@P*>obhc*fdW+C'

# Define Pseudo-Random Function
prf = lambda key, msg:HMAC(key = key, msg = msg, digestmod = HASH).digest()

# Login
ID = bytes(input('ID: '), 'utf-8')
master_password = bytes(input('Password: '), 'utf-8')

# Client-Side Hashing
master_key = SCRYPT(password = master_password, salt = ID, N = 1_024, r = 4, p = 1, dkLen = 32, prf = prf).scrypt()

master_hash = SCRYPT(password = master_key, salt = master_password, N = 1, r = 4, p = 1, dkLen = 64, prf = prf).scrypt()

stretched_master_key = HKDF(input_key_material = master_key, prf = prf, length = 32).hkdf()

# Server-Side Hashing
authentification_key = SCRYPT(password = master_hash, salt = stored_salt, N = 1_024, r = 4, p = 1, dkLen = 128, prf = prf).scrypt()

if authentification_key == auth:
    # Client-Side Decryption
    output_password = AES(stretched_master_key).decrypt_cbc(protected_key, init_vec)

    print(output_password)

######################### MAKE PASSWORD ########################

# Imports
from random import choice

init_vec = bytes(''.join([choice('1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:ZXCVBNM<>?') for _ in range(16)]), 'utf-8')

password = bytes(input('Password: '), 'utf-8')

protected_key = AES(stretched_master_key).encrypt_cbc(password, init_vec)
print(protected_key)