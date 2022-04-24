alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
    encrypted_word = []
    last_index = int(alphabet.index('z'))
    for n in text:
        encrypted_position = int(alphabet.index(n)) + shift
        if encrypted_position > last_index:
            encrypted_position = encrypted_position - last_index - 1
        encrypted_word.append(alphabet[encrypted_position])

    print(f'"The encoded text is {"".join(encrypted_word)}.')

    # TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
    decrypted_word = []
    first_index = int(alphabet.index('a'))
    last_index = int(alphabet.index('z'))
    for n in text:
        encrypted_position = int(alphabet.index(n)) - shift
        if encrypted_position < first_index:
            encrypted_position = last_index + encrypted_position
        decrypted_word.append(alphabet[encrypted_position])

    print(f'"The decoded text is {"".join(decrypted_word)}.')


    # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    # e.g.
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print output: "The decoded text is hello"

    # TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
else:
    print("I can't understand!")