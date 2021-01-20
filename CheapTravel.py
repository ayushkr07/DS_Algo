n,m,a,b=[int(i) for  i in input().split()]


sum=0

if a<=(b/m):
    sum=(n*a)
else:
    if n<m:
        sum=b
    else:
        d1=n//m
        d2=n%m
        sum=(d1*b)+(d2*a)

print(sum)

