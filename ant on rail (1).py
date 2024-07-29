#ant on rail
#there is an ant on your balcony.it wants to lv the rail so smtms it moves right and sometimess it moves left until it gets exhausted.given an integer array A of size N which consists of interger 1 and -1 only reprenting ants moves

#where 1 means ant moved unit distance towards the right side and -1 means it moved unit distance towards the left.your task is to find and return the integer value representing how many times the ant reaches back to original starting position.
#NOTE:assume 1-based indexing 2.assume that the raililng extends infinitely on the either sides
'''N=int(input("enter the no of moves"))
A=list(map(int,input().split()))
sp=0
ans=0
for i in A:
    sp=sp+i
    if sp==0:
        ans=ans+1
print(ans)'''


#vowel repetition problem
n=input("enter the string")
d={"a:0","e:0","i:0","o:0","u:0"}

for i in n:
    if n==d:
        n+=1
print(n)
    

