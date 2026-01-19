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

def exibir_dia_da_semana_if(numero):
    print('Execucao com IF')
    if numero == 1:
       print('O dia e segunda')
    elif numero == 2:
        print('O dia e terca')
    elif numero == 3:
        print('O dia e quarta')
    elif numero == 4:
        print('O dia e quinta')
    elif numero == 5:
        print('O dia e sexta')
    elif numero == 6:
        print('O dia e sabado')
    elif numero == 7:
        print('O dia e domingo')
    else:
        print('Numero de dia invalido. Digite numero de 1 a 7')

def exibir_dia_da_semana_match(numero):
    print('Execucao com MATCH')
    match numero:
        case 1:
           print('O dia e segunda')
           exit()
        case 2:
            print('O dia e terca')
            exit()
        case 3:
            print('O dia e quarta')
            exit()
        case 4:
            print('O dia e quinta')
            exit()
        case 5:
            print('O dia e sexta')
            exit()
        case 6:
            print('O dia e sabado')
            exit()
        case 7:
            print('O dia e domingo')

def brincar_de_para_ou_continua():
    resposta = 'C' # S aqui significa que continua

    while resposta.upper() == 'C':
        resposta = input('Digite P para parar e C para continuar')

    print('você decidiu parar com a brincadeira')

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

    # exemplo de dia da semana com if – elif – else
    exibir_dia_da_semana_if(6)

    # exemplo dia da semana com match - case
    exibir_dia_da_semana_match(2)

    # exemplo com while - para ou continua
    brincar_de_para_ou_continua()




