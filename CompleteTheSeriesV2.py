import math
for _ in range(int(input())):
    third,forthLast,total=[int(i) for i in input().split()]

    a=6
    b=(5*third)+(7*forthLast)-(2*total)
    c=(forthLast**2)-(third**2)

    D=(b**2)-(4*a*c)
    D=math.sqrt(D)


    x1=(-b+D)/(2*a)
    x2=(-b-D)/(2*a)

    if x1.is_integer():
        d=int(x1)
    else:
        d=int(x2)

    a1=third-(2*d)

    n=((forthLast-a1)//d)+4
    print(n)

    for i in range(n):
        print(a1+(i*d),end=" ")