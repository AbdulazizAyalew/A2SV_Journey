t = int(input())
for i in range(t):
    n = int(input())
    a = list(input().split())
    s = ""
    for word in a:
        if word + s < s + word:
            s = word + s
        else:
            s += word
    print(s)
    