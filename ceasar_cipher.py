from turtle import position


alphabet = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
            's','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k',
            'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#print(alphabet)

direction = input("Type 'encode' to encrypt, type 'decode to decrypt\n")
text = input("Type yuor message\n").lower()
shift = int(input("Type the shift number\n"))

#encode function
'''def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

#decode function
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")



if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)'''

#ONE FUCTION FOR ALL
def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == 'encode':
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        elif cipher_direction == 'decode':
            new_position = position - shift_amount
            end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")

ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)