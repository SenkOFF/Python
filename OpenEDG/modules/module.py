print('I like to be a module.')
print(__name__)
print("-"*100, "\n")

__counter = 0

def suml(tlist):
    global __counter
    __counter += 1
    tsum=0
    for element in tlist:
        tsum +=element
    return tsum

def prodl(tlist):
    global __counter
    __counter +=1
    prod=1
    for element in tlist:
        prod *=element
    return prod

if __name__=='__main__':
    print("I prefer to be a module, but I can do some tests for you.")
    mylist=[i+1 for i in range(5)]
    print(suml(mylist) == 15)
    print(prodl(mylist) == 120)
else:
    print("I like to be a module, but I'm working like a slave now.")
    