def fib_topDown(n,memo):
    if memo[n] is not None:
        return memo[n]

    if n==0 or n==1:
        result =  n
    else:
        result  = fib_topDown(n-1,memo)+fib_topDown(n-2,memo)
    memo[n] = result
    return memo[n]


def fib_memo(n):
    memo = [None]*(n+1)
    return fib_topDown(n,memo)


print(fib_memo(7))
