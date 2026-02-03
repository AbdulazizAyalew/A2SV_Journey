t = int(input())

for i in range(t):
    a,b,n = map(int,input().split())
    Tools = list(map(int,input().split()))

    max_Time = b
    for Tool_val in Tools:
        if (Tool_val + b) <= a:
            b += Tool_val
            max_Time += Tool_val
        else:
            if Tool_val > a - 1:
                max_Time += (a - 1)
                b = a
            else:
                max_Time += Tool_val
    print(max_Time)





        