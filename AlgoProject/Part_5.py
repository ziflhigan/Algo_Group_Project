

def decode_caesar_cipher(encoded_message, shift):
    decoded_message = ""

    for char in encoded_message:

        if char.isalpha():

            shifted = ord(char) - shift

            if char.islower():

                if shifted < ord('a'):
                    shifted += 26

            elif char.isupper():

                if shifted < ord('A'):
                    shifted += 26

            decoded_message += chr(shifted)

        else:

            decoded_message += char

    return decoded_message


encoded_message = "Wkh vwdwxh lv exulhg xqghu d wuhh pdunhg zlwk a rq Foxvwhu Lvodqg- 3"

decoded_message = decode_caesar_cipher(encoded_message, 3)

print(decoded_message)