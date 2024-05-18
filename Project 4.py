# Project:Find even and odd numbers from a list, and store them separately in a new list

List=[12,67,98,45,77,65,34,14,79,46,76,27]

Even=[]
Odd=[]

for k in List:
    if k%2==0:
        Even.append(k)

for h in List:
    if h%2==1:
        Odd.append(h)

print("List =",List)
print("Even numbers = ",Even)
print("Odd numbers = ", Odd)