 # a=[1,2,3,4,5]
# count=0
# i=0
# while i<len(a):
#     count=count+a[i]
#     i=i+1
# print(count)

# a=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# i=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum)

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
k=[]
i=0
count=0
while i<len(a):
    k.append(a[i])
    if count==3:
        k.append("20")
        count-=4
    count+=1
    i=i+1
print(k)