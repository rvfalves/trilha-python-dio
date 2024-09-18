def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    numero_vendas = 0
    total_vendas = 0
    for venda in vendas:
        total_vendas += venda
        numero_vendas += 1
    media_vendas = total_vendas/numero_vendas
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    vendas = []
    vendas = list(map(int, entrada.split(", ")))
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))