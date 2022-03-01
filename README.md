# Null_Bit

A crappy string encryption and decryption tool.

Available Ciphers/Encryption methods:

* Cryptography
    * XOR-Cipher
    * Vigenere Cipher
    * Columnar Transposition Cipher
* Steganography
    * Encode message in Images (*.png)

This program was made for the 2022 KMC AFCEA SkillsUSA Programming Competition.

## How it works

1.) User logs in to the program with the default username and password of:
* Username: SKILLSUSA2022
* Password: AFCEA

2.) Decide whether you are going to try and encrypt text or decrypt text from the 
drop down box. Then decide what kind of encryption method you will be using
from the next drop down box.

3.) The user will either load up a *.txt document containing text they want
encrypted or they will put in their own message into the input box.

4.) Once they have their message setup, the user can (depending on the cipher/type 
of encryption they are using) enter a key that they can then use later to 
decrypt the encoded cipher text. 

5.) Now that they have their encryption type, message, and key ready to go, 
all that is left to do is to hit run! Your newly encrypted text can be found in
the output box below the input box. Now that you have your newly encrypted
cipher-text, you can decide if you want to save the output or key with their
respective buttons.

## Dependencies

- Python 3.9.7 or newer
- PyQt5 == 5.14.2
