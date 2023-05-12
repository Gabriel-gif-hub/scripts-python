a = [2,3,4,7]
b = a #isso se torna uma ligação da lista
# uma cópia seria assim = b = a[:]
b[3] = 1
print(f'Lista a:{a}')
print(f'Lista b:{b}')
