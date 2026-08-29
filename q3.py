#function to print individual prime numbers till the number in input
def prime(n):
    for i in range(1,n):

        if n%i==0 and i!=1: #checking for factors
            break #break statement utilised

        else: #case where no factors except 1 and itself
            if i == n-1:
                print(n, " ", end='')

#checking if the number taken as input is prime + printing the prime numbers one by one lesser than it
def is_prime(n):

    c=1 #variable where c=1 means prime, and c=0 means composite

    if n>1:
        for i in range(1,n+1):

            prime(i) #to print prime numbers

            if n%i==0 and i!=1 and i!=n: #checking for factors
                c=0 #number confirmed as composite

            else: #runs when the iteration number 'i' is not the factor of the number 'n'
                if i == n and c==1: #number is prime
                    print()
                    return 'True' 

    else:
        return 'Neither prime nor composite'
    if c==0:
        print()
        return 'False'

#number taken as input
x = int(input("Enter a number: "))

#final output
print(is_prime(x))
