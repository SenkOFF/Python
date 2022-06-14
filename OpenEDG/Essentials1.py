
print("\n")

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    
    print("Happy New Year!")

happy_new_year(False)

print("\n")

EMPTY = "-"
ROOK = "ROOK"
board = []
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
board[4][2] = "KNIGHT"
board[3][4] = "PAWN"
print(board)

print("\n")

for i in range(2, 8, 3):
    print("The value of i is currently", i)

print("\n")

secret_number = 777
print(
"""
+=========================+
| Welcome to my game, muggle!   |
| Enter an integer number              |
| and guess what number I've        |
| picked for you.                           |     
| So, what is the secret number?   |
+=========================+
""")
number = int(input("Guess what number: "))
while number!=secret_number:
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Try again. Guess what number: "))
else:   
    print("Well done, muggle! You are free now.Congratulation, my number is ", secret_number)
    
print("\n")

def calculate(operator, x, y):
  if operator == "+":
    print(x + y)
  elif operator == "-":
    print(x - y)
  else:
    print(f"unknown: {operator}")
calculate("-", 30, 10)

print("\n")

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
# Print the result
print("The larger number is:", larger_number)
print("\n")
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

print("\n")

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

print("\n")

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print("\n")
print(9 % 6 % 2)
print("\n")
print("My name is", "Python.", end=" ")
print ("Hello World.")
print("\n")
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("\n")
print("     *")
print("   *  *")
print("  *    *")
print(" *      *")
print("***   ***")
print("  *    *")
print("  *    *")
print("  *****")

print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

print(111, 111, 111, sep="_", end=" :))")

print("\n")

a=3e8
print(a)

print("\n")

print(0.0000000000000000000001)
b=1e-22
print(b)

print("\n")

print("I like \"Monty Python\"")

print("\n")

print(True > False)
print(True < False)

