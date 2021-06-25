user_input=list(map(str,input("enter a list of words").rstrip().split()))
result=[]
result=user_input[::-1]
result_string=""
for i in result:
    result_string=result_string+i+" "
print(result_string)
