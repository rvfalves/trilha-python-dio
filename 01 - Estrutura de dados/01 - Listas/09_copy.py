lista = [0, "Python", [40, 30, 20]]

l1 = lista

l2 = lista.copy()

print(lista)  # [0, "Python", [40, 30, 20]]

l1[0] = 1
l2[0] = 2

print(lista) # [1, "Python", [40, 30, 20]]
print(l1) # [1, "Python", [40, 30, 20]]
print(l2) # [2, "Python", [40, 30, 20]]