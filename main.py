list=[]
def numbers ():
    for count in range(5):
        list_input = int(input("enter any number to append it to list "))
        list.append(list_input)
        len(list)
    return list

x=numbers()
print(x)
n=int(input("enter number"))
for item in list:
    if item %n ==0:
        print(item)