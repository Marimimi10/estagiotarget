número=int(input("Digite o número a ser analisado: "))

fibonacci = [0, 1]

while fibonacci[-1] < 100:
    fibonacci.append(fibonacci[-2] + fibonacci[-1])

print(fibonacci)
if número in fibonacci: 
   print("O número pertence a sequência Fibonacci")
else:
    print("O número não pertence a sequência Fibonacci")

