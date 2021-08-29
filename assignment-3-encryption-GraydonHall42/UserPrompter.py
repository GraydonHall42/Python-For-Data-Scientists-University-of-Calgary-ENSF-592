# Graydon Hall

import re


class UserPrompter:
    """
    Used to communicate with the user. It includes methods to greet the user, get a message to be encoded or decoded,
    and also obtain a valid cipher from the user, which is a 26 character string containing lowercase letters
    and numbers only.

    :param: no input parameters
    """

    def user_greeting(self):
        """
        Prints a greeting to the user, asking them whether they'd like to encode or decode a message.
        :param: no input parameters
        :return: the users choice as to whether they would like to encode or decode a message.
        """

        while (True):  # execute loop till valid input is provided.
            try:  # try to get user input
                user_choice = int(input("Enter 1 to encode, or 2 to decode your message: "))  # prompt user.
                if (user_choice == 1 or user_choice == 2):  # if valid choice
                    return user_choice  # return users choice.
            except:  # catches error if anything besides 1 or 2 entered.
                print("Invalid entry. You must enter either 1 or 2")  # error message to user.

    def get_encoding_message(self):
        """
        Obtains a message from the user which will be encoded, and formats the message by making all letters lowercase,
        and removing any characters which are nto letters.
        :param: no input parameters
        :return: a properly formatted version of the users message that they wish to encode as a string.
        """

        user_message = input("Please enter the text to be processed: ").lower()
        formatted_message = re.sub(r'[^a-z]', '', user_message)  # remove anything not a letter
        return formatted_message

    def get_decoding_message(self):
        """
        Obtains a message which the user wishes to decode
        :param: no input parameters
        :return: message as a string which will be decoded
        """

        user_message = input("Please enter the text to be processed: ").lower()  # prompt user for message.
        return user_message

    def get_user_cipher(self):
        """
        Obtains cipher from user. Validates cipher to ensure its validity. For cipher to be valid, must be 26 characters
        and only contain lowercase numbers or digits 0-9.
        If invalid cipher is provided, user is informed of error and prompted to re-enter valid cipher.
        :param: no input parameters
        :return: valid cipher used for encoding and decoding.
        """

        # cipher rules: only lowercase a-z or number 0-9, must be 26 characters.
        # ^ anchor denotes start of string
        # $ anchor denotes end of string
        # [a-z0-9] denotes only a-z or 0-9 acceptable
        # {26} denotes exactly 26
        cipher_pattern = r'^[a-z0-9]{26}$'

        while (True):  # execute till valid input is provided
            try:  # try to get valid input
                user_cipher = input("Please enter the cipher text: ")  # obtain user input
                if re.search(cipher_pattern, user_cipher):  # if input is valid
                    return user_cipher  # return valid cipher
                else:  # invalid intput provided
                    raise ValueError  # raise a value error
            except ValueError:
                print("Your cipher must be 26 elements of a-z or 0-9")  # provide user error message
