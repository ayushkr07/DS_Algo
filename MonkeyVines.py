# Input:
# 3
# []
#
# [[][[]]]
#
# Output:
# 1 2
# 2 1
# 3 8

for _ in range(int(input())):
    s=input()
    cnt=0
    for i in s:
        if i=="[":
            cnt+=1
    if cnt==0:
        print(_+1,1)
    else:
        print(_+1,cnt*2)



