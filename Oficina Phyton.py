
#Váriaveis:
print("Váriaveis")
print("  ")
numero = 50
nome = "Richard de Souza"
valor = 55.90
letra = 'x'

#Ação com as váriaveis:
print (numero)
print (nome)
print (valor)
print (letra)
print("  ")

#Comentários neste local:
"""
Comentário com
várias linhas
é separado
com 3 apas simples
"""
#Outro tipo de comentário:
"""
Também pode
ser feito com 3
apas duplas
"""

#Exercício 1:
print("Exercício 1:")
print("  ")
Nome = 'Richard de Souza'
Idade = 19
Altura = 1.65
Peso = 55
Endereço = "Rua Julio Jansem Nº 110"
print ("Nome:",Nome)
print ("Idade:",Idade)
print ("Altura:",Altura)
print ("Peso:",Peso)
print ("Endereço:",Endereço)
print("  ")

#Saída de Dados:
'''
int= %d ou %i
float= %f
string= %s
'''
#Exemplos:
print("Exemplo de Saída de Dados")
print("  ")
print("Nome: %s " % Nome)
print("Idade: %d anos" %Idade)
print("Altura: %.2f" % Altura)
print("Peso: %.2f" % Peso)
print("Endereço: %s" % Endereço)
print("  ")

#Entrada de Dados
'''
input
'''

#Exemplo
print("Exemplo de Entrada de Dados")
print("  ")
#Execício 2:
print("Execício 2:")
#Valores sendo convertidos
nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
idade = int(idade)
altura = input("Digite a sua altura: ")
altura = float(altura)
peso = input("Digite o seu peso: ")
peso = float(peso)
endereco = input("Digite o seu endereço :")

print("Nome: %s " % nome)
print("Idade: %d anos" % idade)
print("Altura: %.2f" % altura)
print("Peso: %.2f" % peso)
print("Endereço: %s" % endereco)
print("  ")

#Operadores Aritméticos
'''
Operadores aritméticos auxiliares em Python
• ** = Potenciação: 2**3 = 8
• math.sqrt = Radiciação: math.sqrt(4) = 2
• % = Resto Divisão: 4 % 3 = 1
Prioridades
• parênteses mais internos
• pot rad
• * / mod
• + -
'''

#Exemplo de operação aritmética
# A soma de dois números inteiros:

print("Soma de dois números inteiros:")
print("  ")

num1 = input('Digite um número inteiro: ')
num2 = input('Digite outro número inteiro: ')
num1 = int(num1)
num2 = int(num2)
soma = num1 + num2

#Três manieras de apresentar o resultado:
print('A soma entre %d e %d vale %d ' % (num1, num2, soma))
print ('A soma entre', num1, 'e', num2, 'vale', soma)
print('A soma entre {} e {} vale {}'.format(num1,num2,soma))
print('')


#Exercícios 3
print("Exercício 3:")
print('')
print ("1 - Desenvolva um programa que receba o salário de um funcionário, calcule e")
print ("mostre seu novo salário com reajuste de 15%")
print("  ")
print ("2 - Desenvolva um programa que receba os valores do comprimento (C), da")
print ("largura (L) e da altura (H) de um paralelepípedo, calcule e mostre o volume")
print ("desse paralelepípedo.")
print("Fórmula do volume de um paralelepípedo: V = C . L . H")
print('')

#Desenvolvimento exercício 3 - 1:
print("Resolução Ex. 1")
print('')
salario = input ("Digite o Valor do seu salário: ")
salario = float(salario)
salario = salario*1.15
print('Novo salario: {}'.format(salario))
print('')

#Desenvolvimento exercicio 3 - 2:
print('Resolução Ex. 2')
print('')
C = input ('Digite o Comprimento: ')
C = float(C)
L = input ('Digite a Largura: ')
L = float(L)
H = input ('Digite a Altura: ')
H = float(H)
V = C * L * H
print("Volume do Paralelepípedo: %.2f" % V)
print('')

#Operadores Relacionais:
'''
• Em pseudocódigo
> maior que 3 > 2 verdadeiro
< menor que 3 < 2 falso
>= maior ou igual que 5 >= 7 falso
<= menor ou igual que 5 <= 7 verdadeiro
= igual 4 = 4 verdadeiro
<> diferente 4 <> 4 falso
• Em Python
> maior que 3 > 2 verdadeiro
< menor que 3 < 2 falso
>= maior ou igual que 5 >= 7 falso
<= menor ou igual que 5 <= 7 verdadeiro
== igual 4 == 4 verdadeiro
!= diferente 4 != 4 falso
'''

#Operadores Lógicos:
'''
• Em pseudocódigo
não negação
e conjunção
ou disjunção
• Em Python
not negação
and conjunção
or disjunção
• Prioridades da esquerda para a direita, de cima para baixo
não
e ou
'''

#Estrutura condicional
'''
•Comando if
• Por exemplo, se o valor da média final for maior ou igual a 5, o aluno
está aprovado:
se (media >= 5)
então mostrar “APROVADO”
• Por exemplo, se o salário bruto for maior que 1000 e menor que
2500, então o percentual de desconto do imposto de renda será de
10%:
se ( (SB >= 1000) e (SB<=2500) )
então IR = 10
• Nestas duas situações existe um teste (condição) para que alguma
operação seja executada.
'''

#Exemplo
print("Exemplo de Estrutura Condicional")
print('')
nota1 = float(input('Entre com a primeira nota: '))
nota2 = float(input('Entre com a segunda nota: '))
media = (nota1 + nota2)/2
if media >=5:
    print('Aprovado com média %.2f' % media)
else:
    print('Reprovado com média %.2f' % media)
print('')

#Identação
'''
• A identação na linguagem Python indica início
de estrutura.
• É obrigatória para iniciar um fluxo de controle.
• Fora isso, dá erro de sintaxe.
'''

#Segundo exemplo de Estrutura Condicional:
print('Segundo exemplo de Estrutura Condicional:')
print('Por exemplo, se o salário bruto for maior que 1000 e menor que')
print('2500, então o percentual de desconto do imposto de renda será de')
print('10%:')
print('')
sb = float(input('Entre com o salário base: '))

if sb >=1000 and sb <=2500 :
    ir = sb * 0.10
    print('Imposto de renda a pagar: %.2f' % ir)

#Terceiro exemplo de Estrutura Condicional:
print('Terceiro exemplo de Estrutura Condicional:')
print('')
#se ( (SB >= 1000) e (SB<=2500) )
#então IR = 10
#senão
#se (SB > 2500)
#então IR = 15
#senão
#IR = 0

sb = float(input('Entre com o salário base: '))
if sb >= 1000 and sb <=2500 :
    ir = sb * 0.10
elif sb > 2500 :
    ir = sb * 0.15
else:
    ir = 0
    print('Imposto de renda a pagar: %.2f' % ir)
print('')

#Exercícios de Fixação
print('Exercícios de Fixação')
print('')
print('1. Fazer um programa para ler dois números inteiros e mostrá-los em')
print('ordem crescente.')
print('2. Fazer um programa para mostrar uma mensagem na tela dizendo')
print('se um número inteiro lido é par ou ímpar.')
print('')

#Estrutura de Repetição Enquanto - Pseudocódigo
'''
• Sintaxe da Estrutura de Repetição enquanto
<inicialização da variável de controle>;
enquanto (<condição>) faça
<comando_1>;
<comando_2>;
...
<comando_n>;
<atualização da variável de controle>;
fimenquanto;
Nota: a <atualização da variável de controle> pode ser feita em qualquer parte
dentro do enquanto, não necessariamente após o último comando.
• Exemplo
x  0;
enquanto (x<3) faça
escreva ("O valor de x é: " , x);
x  x + 1;
fimenquanto;
Nota 1: no exemplo acima, o x é <variável de controle>. É ele que faz parte da
condição do loop.
Nota 2: veja que o x também é usado no processamento dentro do loop. Portanto a
variável x não é de uso restrito ao controle do loop.
'''
"""
Estrutura de Repetição Enquanto - Python
• Sintaxe da Estrutura de Repetição enquanto
<inicialização da variável de controle>;
while <condição> :
<comando_1>;
<comando_2>;
...
<comando_n>;
<atualização da variável de controle>;
"""

#Exemplo While
print('Exemplo While')

x= 0
while x < 3:
    print('O valor de x é: %d' % x)
    x = x + 1
print('Saiu do While')

#Exercícios While
print('Exercícios While')
print('')
print('1. Desenvolva um programa que recebe números)
print('inteiros digitados pelo usuário e calcula a soma entre')
print('esses números e a média. Só parar de digitar os')
print('números quando o usuário digitar zero.')
print('')
print('2. Desenvolva um programa que recebe 10 números')
print('reais digitados pelo usuário e soma somente os')
print('números pares.')
print('')










      



















