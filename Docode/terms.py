#Найти массу, обьем, плотность
choise = input('Введителе искомое: (m, d, v) - ')
if choise == 'm':
    d = float(input('Введите плотность: '))
    v = float(input('Введите обьем: '))
    print('Масса ровна :', d*v)
elif choise == 'd':
    m = float(input('Введите массу: '))
    v = float(input('Введите обьем: '))
    print('Плотность ровна :', m/v)
elif choise == 'v':
    d = float(input('Введите плотность: '))
    m = float(input('Введите массу: '))
    print('Обьем равен :', m/d)
else :
    print('Введена неверная операция')
    
print('-'*100, '\n')

#В какой координатной четверти находится точка
print('''
                   /\          
       2nd quart.  ||  1st quart.   
                   ||
    <==============================>
                   ||
       3rd quart.  ||  4rd quart.                  
                   \/          
        ''')
print('Input coordination:')
x = float(input('x = '))
y = float(input('y = '))
if x>0 and y>0:
    print('You are in 1st quarter!')
elif x<0 and y>0:
    print('You are in 2nd quarter!')
elif x<0 and y<0:
    print('You are in 3rd quarter!')
elif x>0 and y<0:
    print('You are in 4rd quarter!')
elif x==0:
    print('You are on Y os')
elif y==0:
    print('You are on X os')
elif x==0 and y ==0:
    print('You are at point 0')
else:
    print('Mistake data')