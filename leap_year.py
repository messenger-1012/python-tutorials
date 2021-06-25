def is_leap(year):
    leap = False
    if(year%4==0):
        print("4")
        if(year%100!=0):
            print("100")
            leap=True
        else:
            if(year%400==0):
                    print("400")
                    leap=True
    print(leap)                
    
    return leap

year = int(input())
is_leap(year)