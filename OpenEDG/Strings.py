from symtable import Symbol

symbol1 = 'a'
symbol2 = 'A'
symbol3 = ' '

#pokazuje numer pozycji w code point
print(ord(symbol1))
print(ord(symbol2))
print(ord(symbol3))
print(int(ord(symbol1)) - int(ord(symbol2)))
print('''Interesting fact that code point of " " are to same 
like a different between big "A" and small "a" .''')
print('-'*100)

# pokazuje symbol zgodnie z wskazanym numerem w code point
print(chr(99))
print(chr(942))
print('-'*100)

#przeksztalenie strings w list
the_string = 'strings working'

for character in the_string:
    print(character, end=' - ')

print()
print('<->'*10)

print(the_string[0:3])
print(the_string[-4:-1])
print(the_string[0::3])
print('<->'*10)

print('r' in the_string)
print(' ' in the_string)
print('a' in the_string)
print('<->'*10)

print(id(the_string))
print('<->'*10)

print(min(the_string))
print(max(the_string))
print('<->'*10)

print(the_string.index('r'))
print(the_string.index('w'))
print('<->'*10)

print(the_string.count('r'))
print(the_string.count('o'))
print('<->'*10)

print(the_string.endswith('g'))
print(the_string.endswith('re'))
print(the_string.endswith('ing'))
print('-'*100)

# znalezenie odpowiedniego znaczenia w variable
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
print('<->'*10)    
print(the_text.find('the'))