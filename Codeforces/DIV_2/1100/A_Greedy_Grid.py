t = int(input())
for i in range(t):
    n,m = map(int,input().split())

    if m == 1 or n == 1:
            print("NO")
            continue

    if m < 3 and n < 3:
        print("NO") 
    else:
        print("YES")