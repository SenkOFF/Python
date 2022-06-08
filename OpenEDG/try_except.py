#przetwarzanie stroki w list i sumowanie
line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")
  
    
number1 = int(input('First number: '))
number2 = int(input("Second number: "))
try:
    print('1st divided by 2nd - ', number1/number2)
except:
    print('This operational can\'t be done!')
    
    
try:
    x = int(input('Please input the number: '))
    y = 1/x
    print(y)
except ZeroDivisionError:
    print('You can\'t divided by 0')
except ValueError:
    print("You must enter an integer value.")
except:
    print('Something wrong...')
print("THE END.")