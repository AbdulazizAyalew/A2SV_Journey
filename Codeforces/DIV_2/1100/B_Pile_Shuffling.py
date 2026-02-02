
t = int(input())

for i in range(t):
    n = int(input())
    no_operation = 0
    
    for i in range(n):
        pile = list(map(int,input().split()))
        zero_status = pile[0] - pile[2]
        one_status = pile[1] - pile[3]

        if zero_status > 0:
            no_operation += zero_status
        if one_status > 0:
            if zero_status > 0:
                no_operation = no_operation + one_status + pile[2]
            else:
                no_operation += one_status + pile[0]
    print(no_operation)  
