listaDuplicatas = [1, 2, 3, 8, 1, 2, 4, 5, 3, 4, 7, 6, 5, 5, 8, 9]
listaSemDuplicatas = []

while listaDuplicatas:
    elemento = listaDuplicatas.pop(0)
    if elemento not in listaSemDuplicatas:
        listaSemDuplicatas.append(elemento)

listaSemDuplicatas.sort()
    
print("A lista sem duplicatas é: ", listaSemDuplicatas)