# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
summ = 0
for i in range(1000):
    if i%3==0 or i%5==0 :
        summ += i
print('Find the sum of all the multiples of 3 or 5 below 1000:','\n', summ)
print('-'*100, '\n')

# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
mlist = [0, 1, ]
summ2 = 0
for i in range(32):
    i = mlist[-1] + mlist[-2]
    mlist.append(i)
    if i>= 4000000 :
        break
    if i%2==0 :
        summ2 += i
del mlist[0:2]
print('The Fibonacci list: \n', mlist)
print('By considering the terms in the Fibonacci sequence whose values do not exceed four million, \n find the sum of the even-valued terms:','\n', summ2)
print('-'*100, '\n')

# Каков самый большой делитель числа 600851475143, являющийся простым числом?
mlist2 = []

   
print('The prime factor list: \n', mlist2)
print('The largest prime factor of the number 600851475143', mlist2[-1:])