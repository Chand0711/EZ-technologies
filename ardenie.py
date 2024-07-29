#Arduino
n=list(map(int,input().split()))
maxi=-1
s=0
for i in n:
    s=s+i
    if s>maxi:
        maxi=s
print(maxi)        

