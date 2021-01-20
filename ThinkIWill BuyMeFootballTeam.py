for _ in range(int(input())):
    n=int(input())

    mat=[]

    for i in range(n):
        tempMat=[int(t) for t in input().split()]
        mat.append(tempMat)

    income=[]
    outcome=[]
    diff=[]

    for j in range(n):
        sum=0
        for i in range(n):
            sum+=mat[i][j]
        income.append(sum)

    for i in range(n):
        sum=0
        for j in range(n):
            sum+=mat[i][j]
        outcome.append(sum)

    for i in range(n):
        diff.append(income[i]-outcome[i])

    res=0
    for i in range(n):
        if diff[i]>0:
            res+=diff[i]

    print(res)

