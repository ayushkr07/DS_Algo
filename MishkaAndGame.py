n=int(input())
m=0
c=0
for i in range(n):
    a,b=[int(i) for i in input().split()]
    if a>b:
        m+=1
    elif b>a:
        c+=1

if m>c:
    print("Mishka")
elif c>m:
    print("Chris")
else:
    print("Friendship is magic!^^")