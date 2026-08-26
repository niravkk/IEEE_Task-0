def is_prime(n):
    for i in range(2,n):
        if(n%i==0):
            return (True)
            break
    else:
        return (False)

N=int(input())
for j in range(2, N+1):
    print(is_prime(j))
    