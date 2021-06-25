user_input=list(map(str,input("enter the string:").rstrip().split()))
result=[]
def evenwords(user_input):
    for i in user_input:
        if ((len(i))%2==0):
            result.append(i)

evenwords(user_input)
for i in result:
    print(i) 