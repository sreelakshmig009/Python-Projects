import random
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%^&*+()|?-/"
al = alphabets + numbers + symbols
length = 16 # for generating the strongest password
password = "".join(random.sample(al,length))
print(password)