for _ in range(int(input())):
    n=int(input())
    loc=[]
    degree=[]
    for t in range(n):
        l,d=[i for i in input().split()]
        loc.append(l)
        degree.append(int(d))

    degree.sort()

    sec=12
    time=[]
    time.append((degree[-1]-degree[0])*sec)
    for i in range(1,n):
        time.append((360-degree[i]+degree[i-1])*sec)

    print(min(time))



