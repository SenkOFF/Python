a = input()

b = a.split(',')
c = b[0]
d = int(b[1])
e = int(b[2])
f = e - d


print(f'{len(c)} {f} {c[d:e]}')