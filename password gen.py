import random
password_keys = "abcdefghijklmnopqrstuvwxyz1234567890@"
length = int(input("enter the length of your password: "))
password = ""
for x in range(length):
    password += random.choice(password_keys)

print(password)