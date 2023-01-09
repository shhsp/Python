import random

print("Password Generator")

chars = "abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*()01234567890"

number = input("Input number of passwords: ")
number = int(number)

length = input("Password Length: ")
length = int(length)

print("Passwords below:")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)