import string
import random

LETTERS = string.ascii_letters
print(LETTERS)
NUMBERS = string.digits
PUNCTUATION = string.punctuation

#print(PUNCTUATION)

length = int(input("nhap mot so: "))

def password_generator(length):
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

    printable = list(printable)
    random.shuffle(printable)
    random_password = random.choices(printable, k = length)
    random_password = ''.join(random_password)

    return random_password
def main():
    password = password_generator()
    print(password)
if __name__ == "__main__":
    main()

