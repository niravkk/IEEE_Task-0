def is_prime(n):
    """
    The else block executes when the loop doesn't get broken
    meaning no factor has been found which means the number must be prime.
    
    """
    for i in range(2,n):
        if(n%i==0):
            return False
            break
    else:
        return (True)

N=int(input("Enter N: "))
for j in range(2, N+1):
    print(j, ": ", is_prime(j))
    