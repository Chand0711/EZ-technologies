#basket ball
l=[]
g=int(input())
size=int(input())
a=list(map(int,input().split()))
mx=-1
for i in range(0,len(a)-size+1):
    temp=a[i:i+size]
    k,s=1,0
    for j in temp:
        s+=(j*k)
        k+=1
    if s>mx:
        mx=s
print(mx)

o/p:
5
2
1 2 3 4 5
14


a=int(input())
b=int(input())
c=list(map(int,input().split()))
mx=0
