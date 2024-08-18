def lcs2(X,Y):
    m = len(X)
    n = len(Y)
    stack = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0  or j==0:
                stack[i][j] = 0
            elif X[i-1]==Y[j-1]:
                stack[i][j] = 1 + stack[i-1][j-1]
            else:
                stack[i][j] = max(stack[i-1][j],stack[i][j-1])
    return stack[m][n]
