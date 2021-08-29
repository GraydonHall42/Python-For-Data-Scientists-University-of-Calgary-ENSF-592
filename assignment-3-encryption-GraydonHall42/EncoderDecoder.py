# Graydon Hall

import string

# rule: no docstring for init...
# put parameters for init in the class docstring.

class EncoderDecoder:
    """
    A class used to encode and decode a user message, using a 26 character cipher which is provided by the user.
    :param cipher: a 26 character string used to encode or decode a message for the user.

    Attributes
    ----------
    encoding_dict:
        A dictionary which is used by the class to encode messages.
        key: alphabet letter, value = corresponding cipher character
    decoding_dict:
        A dictionary which is used by the class to decode messages
        key: corresponding cipher character, value = alphabet letter
    """


    def __init__(self, cipher):
        cipher_list = list(cipher)  # convert cyhper to list
        alphabet_list = list(string.ascii_lowercase)  # list of the alphabet in order.

        # intitialize empty dictionaries.
        self.encoding_dict = {}
        self.decoding_dict = {}

        for cipher_char, letter in zip(cipher_list, alphabet_list):  # create encoding/decoding dicts
            self.encoding_dict[letter] = cipher_char  # key: alphabet letter, value = corresponding cipher character
            self.decoding_dict[cipher_char] = letter  # key: corresponding cipher character, value = alphabet letter

    def encode_message(self, message):
        """
        Takes a message as a string to be encoded, and encodes it using the cipher provided.
        :param message: message that will be encoded
        :return: encoded message
        """
        encoded_message_list = [self.encoding_dict[char] for char in message]  # encode message
        encoded_message = ''.join(map(str, encoded_message_list))  # convert list to string
        return encoded_message

    def decode_message(self, message):
        """
        Takes a message to be decoded as a string, and decodes it using the cipher provided. Decoded message is all
        lowercase without spaces.
        :param message: message that will be decoded
        :return: decoded message
        """

        decoded_message_list = [self.decoding_dict[char] for char in message]  # decode message
        decoded_message = ''.join(map(str, decoded_message_list))  # convert list to string
        return decoded_message
