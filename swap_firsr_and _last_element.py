list_limit=input("enter the limit:")
list_data=list(map(int,input("enter the list:").rstrip().split()))
saved_list=list_data
print(list_data,"\n",list_limit)
temp=list_data[0]
list_data[0]=list_data[-1]
list_data[-1]=temp
print("orginal list:",saved_list,"\t")
print("swapped list:",list_data)