num = [2,5,7,7]
num[2] = 4
num.append(7)
# num.sort(reverse=True)
print(num)
if 3 in num:
    num.remove(3)
else:
    print('Não temos o 3 na lista')
print(num)
print(f'Essa lista tem {len(num)} elementos')
