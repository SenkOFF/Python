# funkcja przywitannia
def say_hello(name, age):
    print(f"Hello {name} World's!")
    print(f'Your age is {age}')
    print('<->'*10)
    
# wywolanie funkcji
say_hello("Pavel", 32)
say_hello(name="Nesci", age=31)
say_hello("Basia", 7)
say_hello(age=1, name="Kris")
print('My family')

print('\n')

# funcjia zkladania
def numb_sum(num1=5, num2=5):
    print(num1+num2)
    
# wywolanie funkcji
numb_sum(1, 2)
numb_sum(13, 5)
numb_sum(78, 349)
numb_sum()