def filtrar_visuais(lista_visuais):
    # Converter a string de entrada em uma lista
    visuais = lista_visuais.split(", ")
    
    # TODO: Normalize e remova duplicatas usando um conjunto
    normalizada = []
    for visual in visuais:
        normalizada.append(visual.title())
    visuais = set(normalizada)
    
    # TODO: Converta o conjunto de volta para uma lista ordenada:
    lista_final = list(visuais)
    lista_final.sort()
    # Unir a lista em uma string, separada por vírgulas
    return ", ".join(lista_final)

# Capturar a entrada do usuário
entrada_usuario = input()

# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)