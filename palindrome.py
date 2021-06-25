user_input=input("enter a string")
result=user_input[::-1]
if(user_input==result):
    print("is palindrome")
else:
    print("not palindrome")    
print(user_input,result)