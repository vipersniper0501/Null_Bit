

class Vigenere_Cipher():

    cipher_text = ""

    def vigenere(self,
                 text: str,
                 key: str,
                 alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[]{}\\|:;\"\'<>?,./`~ ',
                 encrypt=True
    ):

        for i in range(len(text)):
            letter_n = alphabet.index(text[i])
            key_n = alphabet.index(key[i % len(key)])

            if encrypt:
                value = (letter_n + key_n) % len(alphabet)
            else:
                value = (letter_n - key_n) % len(alphabet)

            self.cipher_text += alphabet[value]


    def encrypt(self, s: str, k: str):
        self.vigenere(text=s, key=k, encrypt=True)


    def decrypt(self, s: str, k: str):
        self.vigenere(text=s, key=k, encrypt=False)
