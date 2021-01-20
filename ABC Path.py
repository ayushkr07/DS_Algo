def isvalid( i, j):
    if (i < 0 or j < 0 or i >= r or j >= c):
        return False
    return True

def isadjacent(prev, curr):
    if (ord(curr) -ord(prev)) == 1:
        return True
    return False


def getLenUtil(mat, i, j, prev):
    if (isvalid(i, j) == False or isadjacent(prev, mat[i][j]) == False):
        return 0

    if (dp[i][j] != -1):
        return dp[i][j]

    ans = 0
    for k in range(8):
        ans = max(ans, 1 + getLenUtil(mat, i + x[k], j + y[k], mat[i][j]))

    dp[i][j] = ans
    return dp[i][j]


def getLen(mat, s):
    for i in range(r):
        for j in range(c):
            dp[i][j]=-1
    ans = 0
    for i in range(r):
        for j in range(c):
            if (mat[i][j] == s):
                for k in range(8):
                    ans = max(ans, 1 + getLenUtil(mat,i + x[k], j + y[k], s))
    return ans
r,c=[int(i) for i in input().split()]

x = [0, 1, 1, -1, 1, 0, -1, -1]
y = [1, 0, 1, 1, -1, -1, 0, -1]

dp=[[0 for i in range(c)]for j in range(r)]

mat=[]
for i in range(r):
    tempMat=[i for i in input().split()]
    mat.append(tempMat)

print(getLen(mat,'a'))


