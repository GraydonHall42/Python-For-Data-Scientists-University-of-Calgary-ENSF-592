# encryption.py
# Graydon Hall
#
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# Detailed specifications are provided via the Assignment 3 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

from EncoderDecoder import EncoderDecoder
from UserPrompter import UserPrompter
import re

def main():
    """
    Main function used to run our encryption program. In this program, user is prompted to either encode
    or decode a message. They enter their message as a string, along with a 26 character cypher. An encoded or decoded
    message is then returned to them.
    """
    print("ENSF 592 Encryption Program")
    prompter = UserPrompter()  # Creat prompter object
    choice = prompter.user_greeting()  # get encode or decode choice

    if (choice == 1):  # user wants to encode
        message = prompter.get_encoding_message()  # get message from user

        cipher = prompter.get_user_cipher()  # get cipher
        encoder_decoder = EncoderDecoder(cipher)  # build our encoder_decoder

        encoded_message = encoder_decoder.encode_message(message)  # encoded version of message
        print(f"Your encoded message is {encoded_message}")  # present to user

    elif (choice == 2): # user wants to decode
        message = prompter.get_decoding_message()  # get message from user

        cipher = prompter.get_user_cipher()  # get cipher
        encoder_decoder = EncoderDecoder(cipher)  # build our encoder_decoder

        decoded_message = encoder_decoder.decode_message(message)  # decoded version of message
        print(f"Your decoded message is {decoded_message}")  # present to user.


def test_encode_decode():
    """
    Method provided for testing purposes on the encoder/decoder.
    A test string is encoded and then decoded using a test cipher.
    """
    test_cipher = '123456ijkfmnopqrstuvwxyzab'
    test_message = '(1) Solution contains at least one regular expression'.lower()
    print(f"Your test mesasge is {test_message}")
    test_formatted_message = re.sub(r'[^a-z]', '', test_message)  # remove anything now a letter
    print(f"Your formatted test mesasge is {test_formatted_message}")
    encoder_decoder = EncoderDecoder(test_cipher)
    encoded_message = encoder_decoder.encode_message(test_formatted_message)
    print(f"your encoded message is: {encoded_message}")
    decoded_message = encoder_decoder.decode_message(encoded_message)
    print(f"your encoded message is: {decoded_message}")

if __name__ == '__main__':
    main()
    # test_encode_decode()


