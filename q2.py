l = eval(input("Enter a list: ")) #using eval to evaulate the datatpye as list

lc = l.copy() #copied list creation

for i in lc:
    if i<0:
        lc.remove(i)

lc.append(0) #appending 0 to the list

lc.sort() #sorting in ascending order (default)

print("Original List: ", l)
print("Modified List: ", lc) #returning of modified list