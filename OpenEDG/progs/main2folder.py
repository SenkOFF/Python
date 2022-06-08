#importowanie i dodanie drogi do FOLDERU projekta do systemowego patchu
from sys import path
path.append('D:\Study\Python\packages')

#importowanie modulej.py lub funkcyj z faila modula.py
from extra.iota import FunI
import extra.good.best.sigma
import extra.good.best.tau  as tau_fun

print(FunI())
print(extra.good.best.sigma.FunS())
print(tau_fun.FunT())
