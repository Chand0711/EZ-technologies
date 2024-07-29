#chocolate jar
'''N=int(input())
A=list(map(int,input().split()))
a=0
r=0
t=0
for i in range(len(A)):
    if A[i]%3==0:
        a=A[i]//3
        t=t+a
    if A[i]%3!=0:
        r=A[i]//3
        a=r+1
        t=t+a
print(t)'''

'''jars=list(map(int,input().split()))
n=int(input())
a=0
for i in jars:
    a=a+(i//3)
    if i%3!=0:
        a=a+1
    else:
        a=a+0
print(a)'''
