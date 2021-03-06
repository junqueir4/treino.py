def moeda(valor=0, tipo='R$'):
    return f'{tipo}{valor:.2f}'.replace('.', ',')


def metade(valor=0, formato=True):
    resposta = valor / 2
    return resposta if formato is False else moeda(resposta)



def dobro(valor=0, formato=True):
    resposta = valor * 2
    return moeda(resposta) if formato else resposta


def aumentar(valor=0, aumento=0, formato=True):
    resposta = valor + (aumento * (valor / 100))
    return moeda(resposta) if formato else resposta


def diminuir(valor=0, porcentagem=0, formato=True):
    resposta = valor - (porcentagem * (valor / 100))
    return moeda(resposta) if formato else resposta
