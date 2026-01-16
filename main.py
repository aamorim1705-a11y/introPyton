# 1 – imports / bibliotecas

# 2 – Classe

# 3 - Metodos e Funções
def print_hi(name):
    print(f'Oi, {name}')

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2

def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento / 2

def realizar_contagem_progressiva(fim):
    for numero in range(fim): # repetir o bloco de 0  ate o fim
        print(numero)         # exibir o numero

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        contador = numero + 1
        print(f'{contador} - {nome}')

#Outra forma de executar a mesma funcao acima
def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        print(numero + 1, ' - ', nome)

# Outra forma de executar a mesma funcao acima
def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        if numero < 9:
           print(0,numero + 1,'-',nome)
        else:
           print(numero + 1,'-',nome)

# Outra forma de executar a mesma funcao acimade forma mais alinhada
def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        if numero < 9:
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero + 1, '-',nome)

# Outra forma de executar a mesma funcao acimade forma mais alinhada
def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        if numero < 9:
           print(f'00{numero + 1} - {nome}')
        elif numero < 99:
           print(f'0{numero + 1} - {nome}')
        else:
           print(numero + 1,'-',nome)

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
           print('PLIM!')
        else:
           print('{:0>3}'.format(numero))

# estrutura de identificação / execução do script
if __name__ == '__main__':
    print_hi('Andrea')

    # chamar a função de cálculo da área do retângulo
    resultado = calcular_area_do_retangulo(3,4)
    print(f'A área do retângulo é de {resultado} m²')

    # chamar a função de calculo da area do quadrado
    resultado = calcular_area_do_quadrado(5)
    print(f'A area do quadrado é de {resultado} m²')

    # chamar a funcao de calculo da area do triangulo
    resultado = calcular_area_do_triangulo(6,7)
    print(f'A area do triangulo é de {resultado} m²')

    # executar uma contagem progressiva
    realizar_contagem_progressiva(11)

    # exibir o nome do candidato varias vezes
    apoiar_candidato('Faker', 100)

    # brincar de plim
    brincar_de_plim(100)

