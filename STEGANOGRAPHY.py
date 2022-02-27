"""
This module is for using steganographic functions in my Null Bit program.
"""

from typing import Union
import os
import cv2
from numpy import typing


class Stego_Image():
    """
    Hides text in image file.

    NOTE: This only works with *.png files!
    """

    cipher_text = ""
    encoded_filepath = ""

    def __char_generator(self, message: str):
        """
        Private Method

        Generator for converting message into unicode numbers.

        :param: message         Message to be encoded in picture
        :yields: unicode number
        """
        for c in message:
            yield ord(c)


    def __get_image(self, path: str) -> Union[typing.NDArray, None]:
        """
        Private Method

        Gets the raw image data out of a file.

        :param: path        Path to image
        :returns: Numpy array of image data of inputted file
        OR
        :returns: None if path is not a file.
        """
        if os.path.isfile(path):
            img = cv2.imread(path)
            return img


    def __gcd(self, x: int, y: int):
        """
        Private Method

        Determines the greatest common denominator of the width and height.
        This is used to determine how far apart we can spread out the encoded
        data.

        :param: x       Width of image
        :param: y       Height of image

        :returns: greatest common denominator
        """
        while y:
            x, y = y, x%y
        return x


    def encode(self, path: str, msg: str, key: str):
        """
        Encodes the message and key into an img file

        :param: path        File path location of image file
        :param: msg         Message to be encoded into image file
        :param: key         Key to be lock/unlock message from image
        """

        img = self.__get_image(path)
        if img is None:
            return
        msg_gen = self.__char_generator(msg+bytes.fromhex("1F").decode("utf-8")+key)
        pattern = self.__gcd(len(img), len(img[0]))

        done = False
        for row in range(len(img)):
            if not done:
                for col in range(len(img[0])):
                    if (row+1 * col+1) % pattern == 0:
                        try:
                            img[row-1][col-1][0] = next(msg_gen)
                        except StopIteration:
                            img[row-1][col-1][0] = 0
                            done = True
                            break
            else:
                break

        filename = "./Encoded_"+path.split('/')[-1]
        self.encoded_filepath = filename
        cv2.imwrite(filename, img)


    def decode(self, path: str, key: str):
        """
        Decodes the message from an img file.
        """

        img = self.__get_image(path)
        if img is None:
            return -1
        pattern = self.__gcd(len(img), len(img[0]))
        decodedMessage = ""
        done = False
        for row in range(len(img)):
            if not done:
                for col in range(len(img[0])):
                    if (row+1 * col+1) % pattern == 0:
                        if img[row-1][col-1][0] != 0:
                            decodedMessage += chr(img[row-1][col-1][0])
                        else:
                            done = True
                            break
            else:
                break
        extractedKey = decodedMessage.split(bytes.fromhex("1f").decode("utf-8"))[1]
        msg = decodedMessage.split(bytes.fromhex("1f").decode("utf-8"))[0]
        if key == extractedKey:
            self.cipher_text = msg
            print(self.cipher_text)
            return 0
        else:
            self.cipher_text = ""
            print(self.cipher_text)
            return -1


#  print(bytes(bytes.fromhex("1F").decode("utf-8").encode("utf-8")).hex()+" in utf-8")
#  steg = Stego_Image()
#  steg.encode("/mnt/c/Users/Michael/Downloads/unknown.png", "Hello World!", "SECRET")
#  steg.decode("/mnt/g/Coding_Projects/Python/Null_Bit/Encoded_unknown.png", "SECRET")
