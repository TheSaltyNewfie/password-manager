# Binary Functions
MAJ = lambda bin1, bin2, bin3:((bin1 | bin2) & bin3) | (bin1 & bin2)
ROTR = lambda bin, n:((bin >> n) | (bin << (8 - n))) % 256
CH = lambda bin1, bin2, bin3:bin3 ^ (bin1 & (bin2 ^ bin3))

# Internal Hashing Functions
f1 = {q:ROTR(q, 7) ^ ROTR(q, 6) ^ ROTR(q, 2) + (q & 1) for q in range(256)}
f2 = {q:ROTR(q, 5) ^ ROTR(q, 3) ^ ROTR(q, 1) + (q & 1) for q in range(256)}
f3 = {q:ROTR(q, 4) ^ ROTR(q, 3) ^ ROTR(q, 2) + (q & 1) for q in range(256)}

# Helper Functions
to_decimal = lambda bin:[int(bin[q:(q + 8)], 2) for q in range(0, 256, 8)]

def split_blocks(padded):
    for q in range(0, len(padded), 256):
        yield to_decimal(padded[q:(q + 256)])

def pad(plaintext):
    binary = ''.join([bin(q)[2:].zfill(8) for q in plaintext])
    end = bin(len(binary))[2:]

    buffer = '0' * (256 - (len(binary) + len(end)) % 256)
    
    return binary + buffer + end

# Hash Class
class HASH:
    def __init__(self, message = b''):
        self.message = message

        self.S_CONST = [*range(16)]
        self.L_CONST = [*range(32)]

    # Concatenation Function
    def update(self, message):
        self.message = b''.join([self.message, message])

    # Copy Class Function
    def copy(self):
        temp = HASH(self.message)
        return temp

    # Define Waterfall Cipher Function
    def waterfall(self, block):
        return [CH(block[q], block[(q + 3) % 32], block[(q + 7) % 32]) ^ MAJ(block[(q - 3) % 32], block[(q - 2) % 32], block[(q - 1) % 32]) for q in range(32)]
    
    # Define Main Cycle Function
    def cycle(self, message_block, hidden_state = [0] * 32):
        for q in range(32):
            temp = message_block[q]

            message_block[q] ^= self.S_CONST[q % 16] ^ self.L_CONST[q % 32] ^ hidden_state[q]

            self.S_CONST[q % 16] = (f1[self.S_CONST[q % 16]] + f2[self.S_CONST[(q - 1) % 16]] + f3[temp]) % 256
            self.L_CONST[q % 32] = (f3[self.L_CONST[q % 32]] + f2[self.L_CONST[(q - 1) % 32]] + f1[temp]) % 256

        return message_block

    # Digest Function
    def digest(self):
        padded = pad(self.message)

        hidden_state = [0] * 32
        for block in split_blocks(padded):
            hidden_state = self.cycle(block, hidden_state)
            hidden_state = self.waterfall(hidden_state)

            self.S_CONST, self.L_CONST = self.L_CONST[16:], self.S_CONST + self.L_CONST[:16]

        output = self.cycle(hidden_state)
        output = self.waterfall(output)

        output = [(q + w) % 256 for q, w in zip(output, self.L_CONST)]

        return bytes(output)
