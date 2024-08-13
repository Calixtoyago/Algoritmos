fibonacci = [1, 1]
n1 = 1
n2 = 1
for c in range(8):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    fibonacci.append(n3)

print(fibonacci)
