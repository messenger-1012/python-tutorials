def swap_case(s):
    result=""
    for i in s:
        if(i.isupper()):
            a=i.lower()
            result=result+a
        elif(i.islower()):
            a=i.upper()
            result=result+a            
        else:
            result=result+i
        
            
            
        
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)