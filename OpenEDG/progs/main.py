from sys import path

path.append('D:\Study\Python')

import modules.module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]

print(modules.module.suml(zeroes))
print(modules.module.prodl(ones))
print("-"*100, "\n")

print(modules.module.__counter)
print("-"*100, "\n")
print(f'module.py id - {id(modules.module)}')