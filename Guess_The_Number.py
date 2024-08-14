l, h = 1, 1000
def guess():
    return l + int((h-l)/2)
m = guess()

feedback = ""


print(m)

while feedback != "correct":
    feedback = input()
    if feedback == "lower":
        h = m 
        m = guess()
        print(m)    
    elif feedback == "higher":
        l = m + 1
        m = guess()
        print(m)