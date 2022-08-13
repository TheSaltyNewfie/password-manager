# https://en.wikipedia.org/wiki/HMAC

# Hashed Message Authentification Code Class
class HMAC:
    def __init__(self, key, msg = None, digestmod = ''):
        if len(key) > 64:
            key = digestmod(key).digest()

        key = key.ljust(64, b'\0')

        self.inner = digestmod(key.translate(bytes((x ^ 0x36) for x in range(256))))
        self.outer = digestmod(key.translate(bytes((x ^ 0x5C) for x in range(256))))

        self.inner.update(msg)

    # HMAC Function
    def digest(self):
        h = self.outer.copy()
        h.update(self.inner.digest())
        return h.digest()
