def find_leargest(number):
    if not number:
        return None

    leargest = number[0]

    for num in number:
        if num > leargest:
             leargest = num

    return leargest

number=[]
num_in=int(input("enter number of elements :"))
for i in range(0,num_in):
    list_entry=int(input())
    number.append(list_entry)
    print(number)

result= find_leargest(number)
print(result)