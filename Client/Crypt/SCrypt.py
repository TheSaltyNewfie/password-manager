# https://en.wikipedia.org/wiki/Scrypt

# Imports
import struct

# Password Based Key Derivation Function2 
def pbkdf2_single(password, salt, key_len, prf):
    block_num = 1
    output = b''

    while len(output) < key_len:
        output += prf(password, salt + struct.pack('>L', block_num))
        block_num += 1

    return output[:key_len]

# Salsa20 Cipher Function
def salsa20_8(B):    
    x = B[:]
    
    for _ in range(4):
        a = (x[0] + x[12]) & 0xffffffff
        x[4] ^= ((a << 7) | (a >> 25))

        a = (x[4] + x[0]) & 0xffffffff
        x[8] ^= ((a << 9) | (a >> 23))

        a = (x[8] + x[4]) & 0xffffffff
        x[12] ^= ((a << 13) | (a >> 19))

        a = (x[12] + x[8]) & 0xffffffff
        x[0] ^= ((a << 18) | (a >> 14))

        a = (x[5] + x[1]) & 0xffffffff
        x[9] ^= ((a << 7) | (a >> 25))

        a = (x[9] + x[5]) & 0xffffffff
        x[13] ^= ((a << 9) | (a >> 23))

        a = (x[13] + x[9]) & 0xffffffff
        x[1] ^= ((a << 13) | (a >> 19))

        a = (x[1] + x[13]) & 0xffffffff
        x[5] ^= ((a << 18) | (a >> 14))
        
        a = (x[10] + x[6]) & 0xffffffff
        x[14] ^= ((a << 7) | (a >> 25))
        
        a = (x[14] + x[10]) & 0xffffffff
        x[2] ^= ((a << 9) | (a >> 23))
        
        a = (x[2] + x[14]) & 0xffffffff
        x[6] ^= ((a << 13) | (a >> 19))
        
        a = (x[6] + x[2]) & 0xffffffff
        x[10] ^= ((a << 18) | (a >> 14))
        
        a = (x[15] + x[11]) & 0xffffffff
        x[3] ^= ((a << 7) | (a >> 25))
        
        a = (x[3] + x[15]) & 0xffffffff
        x[7] ^= ((a << 9) | (a >> 23))
        
        a = (x[7] + x[3]) & 0xffffffff
        x[11] ^= ((a << 13) | (a >> 19))
        
        a = (x[11] + x[7]) & 0xffffffff
        x[15] ^= ((a << 18) | (a >> 14))
        
        a = (x[0] + x[3]) & 0xffffffff
        x[1] ^= ((a << 7) | (a >> 25))
        
        a = (x[1] + x[0]) & 0xffffffff
        x[2] ^= ((a << 9) | (a >> 23))
        
        a = (x[2] + x[1]) & 0xffffffff
        x[3] ^= ((a << 13) | (a >> 19))
        
        a = (x[3] + x[2]) & 0xffffffff
        x[0] ^= ((a << 18) | (a >> 14))
        
        a = (x[5] + x[4]) & 0xffffffff
        x[6] ^= ((a << 7) | (a >> 25))
        
        a = (x[6] + x[5]) & 0xffffffff
        x[7] ^= ((a << 9) | (a >> 23))
        
        a = (x[7] + x[6]) & 0xffffffff
        x[4] ^= ((a << 13) | (a >> 19))
        
        a = (x[4] + x[7]) & 0xffffffff
        x[5] ^= ((a << 18) | (a >> 14))
        
        a = (x[10] + x[9]) & 0xffffffff
        x[11] ^= ((a << 7) | (a >> 25))
        
        a = (x[11] + x[10]) & 0xffffffff
        x[8] ^= ((a << 9) | (a >> 23))
        
        a = (x[8] + x[11]) & 0xffffffff
        x[9] ^= ((a << 13) | (a >> 19))
        
        a = (x[9] + x[8]) & 0xffffffff
        x[10] ^= ((a << 18) | (a >> 14))
        
        a = (x[15] + x[14]) & 0xffffffff
        x[12] ^= ((a << 7) | (a >> 25))
        
        a = (x[12] + x[15]) & 0xffffffff
        x[13] ^= ((a << 9) | (a >> 23))
        
        a = (x[13] + x[12]) & 0xffffffff
        x[14] ^= ((a << 13) | (a >> 19))
        
        a = (x[14] + x[13]) & 0xffffffff
        x[15] ^= ((a << 18) | (a >> 14))

    for q in range(16):
        B[q] += x[q]
        B[q] &= 0xffffffff
    
    return B

# Block Mix Salsa Function
def blockmix_salsa8(BY, Yi, r):
    start = (2 * r - 1) * 16
    X = BY[start:(start + 16)] 

    for q in range(r * 2):
        for w in range(16):
            X[w] ^= BY[q * 16 + w]                  

        X = salsa20_8(X)                                              
        aod = (q * 16) + Yi
        BY[aod:(aod + 16)] = X[:16]

    for q in range(r):
        aos = (q * 32) + Yi
        aod = q * 16
        BY[aod:(aod + 16)] = BY[aos:(aos + 16)]

    for q in range(r):
        aos = ((q * 2 + 1) * 16) + Yi
        aod = (q + r) * 16
        BY[aod:(aod + 16)] = BY[aos:(aos + 16)]

    return BY

# SCrypt Mix Function
def smix(B, Bi, r, N):
    V = [0] * (r * 64)
    X = [0] * (N * r * 32)
    X[:(r * 32)] = B[Bi:(Bi + (r * 32))]

    for q in range(N):
        aod = r * 32 * q
        V[aod:(aod + (r * 32))] = X[:(r * 32)]
        X = blockmix_salsa8(X, r * 32, r)

    for q in range(N):
        j = X[((r * 2) - 1) * 16] & (N - 1)
        for w in range(r * 32):
            X[w] ^= V[(j * 32 * r) + w]
        
        X = blockmix_salsa8(X, r * 32, r)

    B[Bi:(Bi + (r * 32))] = X[:(r * 32)]

    return B

# SHA Based Crypto Hashing Class
class SCRYPT:
    def __init__(self, password, salt, N, r, p, dkLen, prf):
        self.prf = prf

        self.password = password
        self.dkLen = dkLen
        self.salt = salt
        self.N = N
        self.r = r
        self.p = p

    # S-Crypt Function
    def scrypt(self):
        B = [q for q in pbkdf2_single(self.password, self.salt, self.p * 128 * self.r, self.prf)]
        B = [(B[q] | (B[q + 1] << 8) | (B[q + 2] << 16) | (B[q + 3] << 24)) for q in range(0, len(B), 4)]

        for q in range(self.p):
            B = smix(B, q * 32 * self.r, self.r, self.N)

        Bc = []
        for q in B:
            Bc += [q & 0xff]
            Bc += [(q >> 8) & 0xff]
            Bc += [(q >> 16) & 0xff]
            Bc += [(q >> 24) & 0xff]

        return pbkdf2_single(self.password, bytes(Bc), self.dkLen, self.prf)
