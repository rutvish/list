# write a programe to find a product of given number:

i=int(input("enter the number:"))
prod=1
while i>0:
    prod=prod*(i%10)
    i=i//10
print("product digit =" , prod)

