a = float(input())
b = float(input())
c = float(input())
perimetro = a + b + c
area = ((a + b)* c)/2
if a + b > c and a + c > b and c + b > a:
    print(f"Perimetro = {perimetro:.1f}")
else:
  print(f"Area = {area:.1f}")