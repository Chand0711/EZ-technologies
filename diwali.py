#diwali
p=int(input())
t=int(input())
l=240-t
rem=0
for i in range(1,p+1):
    rem=5*i+rem
    a=l-rem
    if a>0:
        n=i
print(n)
