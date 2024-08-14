expected = ['1', '2', '3', '4', '5']
s = input().split(" ")

def _print():
    print(*s)

while s != expected:
    if s[0] > s[1]:
        s[0], s[1] = s[1], s[0]
        _print()
    if s[1] > s[2]:
        s[1], s[2] = s[2], s[1]
        _print()
    if s[2] > s[3]:
        s[3], s[2] = s[2], s[3]
        _print()
    if s[3] > s[4]:
        s[4], s[3] = s[3], s[4]
        _print()



