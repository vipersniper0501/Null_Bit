import math

class Columnar_Cipher():

    cipher_text = ""


    def encrypt(self, msg: str, key: str):
        """
        Encrypt provided plain text with columnar transposition cipher
        using the provided key.

        :param: msg         Message to be encrypted
        :param: key         Key to encode message with
        """
        # track key indices
        k_indx = 0

        msg_len = float(len(msg))
        msg_lst = list(msg)
        key_lst = sorted(list(key))

        # calculate column of the matrix
        col = len(key)

        # calculate maximum row of the matrix
        row = int(math.ceil(msg_len / col))

        # add the padding character '_' in empty
        # the empty cell of the matix 
        fill_null = int((row * col) - msg_len)
        msg_lst.extend('_' * fill_null)

        # create Matrix and insert message and 
        # padding characters row-wise 
        matrix = [msg_lst[i: i + col] 
                  for i in range(0, len(msg_lst), col)]

        # read matrix column-wise using key
        for _ in range(col):
            curr_idx = key.index(key_lst[k_indx])
            self.cipher_text += ''.join([row[curr_idx] 
                              for row in matrix])
            k_indx += 1

    def decrypt(self, cipher: str, key: str):
        """
        Decrypts provided cipher text with the provided key.

        :param: cipher      Cipher text to decode
        :param: key         Key to encode message with
        """
        # track key indices
        k_indx = 0

        # track msg indices
        msg_indx = 0
        msg_len = float(len(cipher))
        msg_lst = list(cipher)

        # calculate column of the matrix
        col = len(key)

        # calculate maximum row of the matrix
        row = int(math.ceil(msg_len / col))

        # convert key into list and sort 
        # alphabetically so we can access 
        # each character by its alphabetical position.
        key_lst = sorted(list(key))

        # create an empty matrix to 
        # store deciphered message
        dec_cipher = []
        for _ in range(row):
            dec_cipher += [[None] * col]

        # Arrange the matrix column wise according 
        # to permutation order by adding into new matrix
        for _ in range(col):
            curr_idx = key.index(key_lst[k_indx])

            for j in range(row):
                try:
                    dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                except IndexError:
                    dec_cipher[j][curr_idx] = "."
                msg_indx += 1
            k_indx += 1

        # convert decrypted msg matrix into a string
        try:
            self.cipher_text = ''.join(sum(dec_cipher, []))
        except TypeError:
            raise TypeError("This program cannot",
                            "handle repeating letters.")

        null_count = self.cipher_text.count('_')

        if null_count > 0:
            self.cipher_text = self.cipher_text[: -null_count]

