def shift_char(letter, shift):
    if letter.isalpha():
        start = ord('A') if letter.isupper() else ord('a')
        return chr((ord(letter) - start + shift) % 26 + start)
    else:
        return letter

def encode(plain_text, shift):
    return ''.join(shift_char(letter, shift) for letter in plain_text)

def decode(plain_text, shift):
    return encode(plain_text, -shift)

goAgain = True
while goAgain:

    print("Do you want to encode or decode? Type 'encode' or 'decode'")
    choice = input().lower()

    if choice == 'encode':
        print("Type your message:")
        message = input()
        print("Type the shift number:")
        shift = int(input())
        encoded_message = encode(message, shift)
        print(f"Encoded message: {encoded_message}")

    elif choice == 'decode':
        print("Type your message:")
        message = input()
        print("Type the shift number:")
        shift = int(input())
        decoded_message = decode(message, shift)
        print(f"Decoded message: {decoded_message}")

    else:
        print("Invalid choice. Please type 'encode' or 'decode'.")
        continue



    print("Do you want to try again? Type 'yes' or 'no'")
    answer = input().lower()

    while answer not in ('yes', 'no'):
        print("Invalid input. Please type 'yes' or 'no'.")
        answer = input().lower()

    if answer == 'yes':
        goAgain = True
    else:
        goAgain = False