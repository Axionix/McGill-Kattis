n = int(input())

L = [list(map(int, input().split())) for _ in range(n)]

L.sort(key=lambda x: x[-1])

i = 0
while i != len(L)-1:
    while L[i][1] > L[i+1][0]:
        L.remove(L[i+1])
    i += 1
        
print(len(L))