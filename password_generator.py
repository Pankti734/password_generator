import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']
no_letters=int(input("How many number of letters do you want?"))
no_numbers=int(input("How many number of numbers do you want?"))
no_symbols=int(input("How many number of symbols do you want?"))
password_list=[]
for char in range(1,no_letters+1):
  password_list+=random.choice(letters)
for char in range(1,no_numbers+1):
  password_list+=random.choice(numbers)
for char in range(1,no_symbols+1):
  password_list+=random.choice(symbols)
print(password_list)
password=random.shuffle(password_list)
for char in password_list:
   password+=char
print(password)
 
  
