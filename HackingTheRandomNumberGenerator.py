n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]

cnt=0

# Brute Force Method
# for i in range(n):
#     for j in range(n):
#         if a[i]+k==a[j]:
#             cnt+=1
#
# print(cnt)

d={}
for i in a:
    if i in d:
        pass
    else:
        d[i]=1

for i in a:
    if k+i in d:
        cnt+=1

print(cnt)