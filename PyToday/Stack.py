#Zadajemy stack jako list
stack = []

print('Current stack: ', stack)
print('\nPush items to the stack')

#Dodajemy znaczenie do stack'u
for i in range(7):
    #Push znaczenie do stack'u
    stack.append(i)
    print('Current stack: ', stack, "\tStack size: ", len(stack))
    
print('\nPop items from the stack')

#Kasujemy(wyjmujemy) znaczenia ze stack'u
while len(stack)>0:
    #Pop znaczenie ze stack'u
    stack.pop()
    print('Current stack: ', stack, '\tStack size: ', len(stack))