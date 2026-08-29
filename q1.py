n = int(input("Enter the number n: ")) #number of no input
l = []
x = 0
for i in range(n): #loop to input individual numbers
  x = int(input("Enter number: "))
  l.append(x)

l1 = l
l.sort()
print("Largest: ", l[-1]) #largest number
print("Smallest: ", l[0]) #smallest number
print("Sum: ", sum(l)) #sum

e = 0
o=0
for i in l: #calculating even and odd count
  if i%2==0:
    e+=1
  else:
    o+=1

print("Even count: ", e)
print("Odd count: ", o)

lr =[] #generating reversed list
for i in range(n-1, -1, -1):
  lr.append(l1[i])

print("Reversed List: ", lr)
