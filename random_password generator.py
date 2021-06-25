import random
finalpassword=""
pass_limit=int(input("enter the password limit:"))
letter_list=list(map(chr, range(32, 123)))
letter_list.remove(" ") #to remove space
def random_char():
    return random.choice(letter_list)
for i in range(0,pass_limit):
    finalpassword=finalpassword+random_char()    
print("your random password is:"+finalpassword)
