from os import urandom

class XOR_Cipher():
    
    key = None
    cipher_text = None

    def genkey(self, length: int) -> bytes:
        """Generate Key"""
        return urandom(length)

    def xor_strings(self, s, t) -> bytes:
        """xor two strings together"""
        if isinstance(s, str):
            # Text strings contain single characters
            return b"".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
        else:
            # Bytes objects contains integer values in the range 0-255
            return bytes([a ^ b for a, b in zip(s, t)])

    def encrypt(self, s:str):
        self.key = self.genkey(len(s))
        self.cipher_text = self.xor_strings(s.encode("ISO-8859-1"), self.key)

    def decrypt(self, s: str, k: str):
        self.cipher_text = self.xor_strings(
            s.encode("ISO-8859-1").decode('unicode-escape').encode("ISO-8859-1"),
            k.encode("ISO-8859-1").decode('unicode-escape').encode("ISO-8859-1")
        ).decode("ISO-8859-1")
