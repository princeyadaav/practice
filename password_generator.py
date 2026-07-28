import random
numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r\n'
           's','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K\n'
           'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_symbols = ['!','@','#','$','%','&','*','(',')','+','_']
print("Welcome to password generator:")
letter =int(input("How many letters you want to in your password: \n"))
symbol =int(input("How many special symbol you want in your password: \n"))
number = int(input("How many numbers you want in your password: \n"))
p = " "
for password in range(letter):
    l = random.choice(letters)
    p = p +l
for password in range(symbol):
    s = random.choice(special_symbols)
    p = p + s
for password in range(number):
    n = random.choice(numbers)
    p = p +n
print(p)    