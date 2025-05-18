text = 'Hello Zaira'
custom_key = 'python'

def vigenere (message, key): 
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
            key_char = key [key_index% len(key)]
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

encryption = encrypt(text, custom_key)
decryption = decrypt(text, custom_key)

print(f'\nEncrypted_text: {text}')
print(f'\nKey: {custom_key}')
print(f'\nDecrypted_text: {decryption}\n')
