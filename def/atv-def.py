# Crie uma função que receba um nome e imprima uma saudação personalizada.
# def msg():
#     nome = input("Informe seu nome: ")
#     print(f"Ola {nome} seja bem vindo(a)")
# msg()

#=============================================================================================

# Crie uma função que receba dois números e retorne sua soma.
# def soma():
#     a = int(input("Informe o primeiro numero: "))
#     b = int(input("Informe o segundo numero: "))
#     print(f"A soma de dos dois numeros é: {a+b}")
# soma()

#=============================================================================================

# Escreva uma função que calcule o quadrado de um número.
# def quadrado():
#     a = int(input("Informe um numero: "))
#     print(f"O quadrado de {a} é: {a**2}")
# quadrado()

#=============================================================================================

# Escreva uma função que verifique se um número é par.
# def par(a):
#     if a % 2 == 0:
#         print("O numero digitado é par")
#     else:
#         print("O numero digitado é impar")
# x = int(input("Informe um numero: "))
# par(x)
 
#=============================================================================================

# Escreva uma função que receba uma lista de números e retorne o maior elemento.
# def lista():

#=============================================================================================

# Crie uma função que calcule o fatorial de um número (sem usar recursão).


#=============================================================================================

# Crie uma função que receba um número e retorne True se ele for primo.
# def num():
#     import math
#     numero = int(input("Digite um numero: "))
#     raiz = math.sqrt(numero) #esse é o jeito importando 
#     raiz = numero**0.5 #um jeito de fazer a raiz quadrada sem importar math
    
#     if numero % raiz:
#         print("O numero é primo")
#     else:
#         print("O numero nao é primo")
# num()


# Crie uma função que inverta uma string.
# def string():
#     texto = input("Informe um numero: ")
#     invertida = texto[::-1]
#     print(f"a frase invertida é: {invertida}")
    
# string()

# Crie uma função que receba uma lista de nomes e retorne apenas os nomes com mais de 5 letras.
# def verificar_nome(a):
#     if len(a) > 5:
#         print("Nome com mais de 5 letras:", a)
#     else:
#         print("Nome com 5 letras ou menos.")

# nome_digitado = input("Digite um nome: ")
# verificar_nome(nome_digitado)

# Escreva uma função que conte quantas vogais há em uma string.
# def contar_vogais():
#     texto = input("Digite uma frase: ")
#     vogais = "aeiouAEIOU"
#     contador = 0
#     for letra in texto:
#         if letra in vogais:
#             contador += 1
#     print(f"A frase tem {contador} vogais.")
# contar_vogais()


# Crie uma função que receba um número e retorne uma lista com todos os divisores dele.
# def divisores():
#     numero = int(input("Digite um número: "))
#     lista_divisores = []
#     for i in range(1, numero + 1):
#         if numero % i == 0:
#             lista_divisores.append(i)
#     print("Divisores:", lista_divisores)
# divisores()



# Crie uma função que converta graus Celsius para Fahrenheit.
# def converter():
#     celsius = float(input("Informe a temperatura em Celsius: "))
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"{celsius}°C em Fahrenheit é: {fahrenheit}°F")
# converter()



# Crie uma função que receba uma string e retorne a mesma string sem espaços.
# def remover_espacos(texto):
#     return texto.replace(" ","")
# frase = input("Digite uma frase para remover os espaços: ")
# resultado = remover_espacos(frase)
# print(resultado)
#.replace(" ", "") troca cada espaço por nada

# Crie uma função que receba uma lista e retorne a média dos elementos.
# def calcular_media(lista):
#     return sum(lista) / len(lista)

# numeros = input("Digite números separados por vírgula: ")
# lista = [float(n) for n in numeros.split(",")]
# media = calcular_media(lista)
# print("A média é:", media)

# Escreva uma função que receba uma palavra e retorne True se ela for um palíndromo.
# def ver_palindromo():
#     palavra = input("escreva uma só palavra: ")
#     ao_contrario = palavra[::-1]
#     if palavra == ao_contrario:
#         print("É um palindromo")
#     else:
#         print("Não é um palindromo")

# Crie uma função que gere uma lista com os n primeiros números pares.
def gerar_pares():
    n = int(input("Quantos números pares você quer? "))

    # Cria uma lista de pares, multiplicando por 2
    pares = []
    for i in range(n):
        pares.append(i * 2)

    # Mostramos a lista de pares
    print("Números pares:", pares)


# Escreva uma função que receba um número e retorne a tabuada dele (de 1 a 10).

# Crie uma função que calcule a área de um retângulo (base × altura).

# Crie uma função que retorne o menor valor entre três números.

# Escreva uma função que simule o lançamento de um dado de 6 faces (use random.randint).