import random
import string

length = int(input("Please enter the length of the password: "))
number = int(input("Please enter the number of numbers: "))
letters = int(input("Please enter the number of letters: "))
symbols = int(input("Please enter the number of symbols: "))
Password_length = number + letters + symbols

if length != Password_length:
    print ("Sorry, the length of the password does not match the number written??")
else:
    number_password = random.choices(string.digits, k=number)
    letters_password = random.choices(string.ascii_letters, k=letters)
    symbols_password = random.choices(string.punctuation, k=symbols)
    info_user_password = number_password + letters_password + symbols_password
    random.shuffle(info_user_password)
    password = ("".join(info_user_password))
    print (f"The password has been created  {password}")