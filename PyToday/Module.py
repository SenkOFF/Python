# importowanie matematycznego modula
import math
for name in dir(math):
    print(name, end="\t")
print("\n", "-"*100, "\n")

#importowanie randomnego znaczenia
from random import random
for i in range(5):
    print(random())
print("-"*100, "\n")

# importowanie konkretnuch funkcij z modula
from platform import platform, machine, processor, system, version
print(platform())
print(machine())
print(processor())
print(system())
print(version())
print("-"*100, "\n")