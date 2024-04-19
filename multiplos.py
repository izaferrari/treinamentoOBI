a = int(input())
b = int(input())
if (a > b and a % b == 0) or (b > a and b % a == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
