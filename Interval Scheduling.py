n = int(input())

L = [list(map(int, input().split())) for _ in range(n)]

L.sort(key=lambda x: x[-1])

ans = 1

x = L[0][1]
for i in L[1:]:
    if i[0] >= x:
        ans += 1
        x = i[1]
        
print(ans)