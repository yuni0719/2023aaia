a = list(map(int, input().split() ))

#print( sum(a) - a[0] )

ans = 0
N = a[0]
for i iAn range(1, N+1):
	ans += a[i]
	
print(ans)