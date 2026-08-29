def prime(n):
    for i in range(1,n):
        if n%i==0 and i!=1:
            break
        else:
            if i == n-1:
                print(n, " ", end='')

def is_prime(n):
    if n>1:
        for i in range(1,n):
            prime(i)
            if n%i==0 and i!=1:
                print()
                return 'False'
                break
            else:
                if i == n-1:
                    print()
                    return 'True'
    else:
        print('Neither prime nor composite')

x = int(input("Enter a number: "))
print(is_prime(x))
