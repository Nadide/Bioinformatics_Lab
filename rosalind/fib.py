dp = {0:0, 1:1, 2:1}

def fib (n, k):
	if n in dp:
		return dp[n]
	else:
		dp[n] = fib(n-1,k) + k*fib(n-2,k)
		return dp[n]

n, k = map(int,input().split(" "))
fib(n,k)
print(dp[n])