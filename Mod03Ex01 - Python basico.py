#!/usr/bin/env python
# coding: utf-8

# ### 01 - Teste de gravidez
# Escreva uma célula com controle de fluxos que tem como premissa a existência das seguintes variáveis:
# 
# - ```sexo``` como ```str``` indicando os valores '**M**' para masculino e '**F**' para feminino  
# - ```beta_hcg``` que indica a quantidade do beta-HCG no sangue em mUI/mL.
# 
# A sua tarefa é escrever um código que imprima como resultado "indivíduo do sexo masculino" quando sexo = 'M', caso sexo = 'F', se o valor de beta-HCG for maior que 5, retorne "Positivo" indicando que a paciente está grávida, e retorne "Negativo" caso contrário.
# 
# Não mexa nos valores da variável ```sexo``` nem em ```beta_hcg```, e escreva um código que funcione para quaisquer valores possíveis de ambos: ```sexo``` = '**M**' ou '**F**' e ```beta_hcg``` assumindo valores inteiros positivos.

# In[1]:


sexo = 'M'
beta_hcg = 0

# seu código vem abaixo desta linha

if sexo == 'M':
    print("indivíduo do sexo masculino")
elif sexo == 'F' and beta_hcg > 5:
    print("Positivo")
else:
    print("Negativo")


# ### 02 - Renomeando variáveis
# 
# Vamos ver adiante que uma forma de renomear variáveis de um conjunto de dados é através de dicionários - o dicionário deve conter como chave o nome original, associando a cada chave um único valor (tipo *str*) que contenha o nome novo.
# 
# A sua tarefa é escrever um dicionário que possa ser utilizado para traduzir as variáveis ```name``` (nome), ```age``` (idade) e ```income``` (renda). Ou seja, esse dicionário deve relacionar as chaves *name, age* e *income* às suas respectivas traduções.

# In[2]:


dic_renomeacao = {'name': 'nome', 'age': 'idade', 'income': 'renda'}
dic_renomeacao


# ### 03 - É divisível?
# A sua tarefa é escrever um código que indique se um número ```N``` é divisível por um número P. Escreva um programa que faça essa verificação para quaisquer combinações de ```N``` e ```M``` e devolva uma mensagem indicativa no output.

# In[3]:


N = 42
M = 7

#Seu código
N = int(input("Digite o valor de N: "))
P = int(input("Digite o valor de P: "))

if N % P == 0:
    print(f"{N} é divisível por {P}.")
else:
    print(f"{N} não é divisível por {P}.")


# ### 04 - Números primos
# > Um número **N** é primo se e somente se é divisível por 1, -1, por **N** e por -**N**.  
# 
# Escreva um script que verifica se ```N``` é um número primo, verificando se ```N``` é divisível por todos os números de ```1``` a ```N-1```. Você vai precisar usar alguma ferramenta de *loop* que você aprendeu para isto. No final, devolva uma mensagem no output indicando se o número é primo ou não.

# In[4]:


N = 47

# seu código abaixo
primo = True

for i in range(2, N):
    if N % i == 0:
        primo = False
        break

if primo:
    print(f"{N} é um número primo.")
else:
    print(f"{N} não é um número primo.")


# ### 05 - Desafio
# O algorítmo do exercício anterior não é o mais eficiente. O que você pode fazer para deixá-lo mais eficiente? Ou seja, executar menos comparações, portanto consumir menos tempo.
# 1. Será que precisamos correr o loop até o final sempre?
# 2. Será que precisamos mesmo verificar **todos** os números?
# 3. Será que precisamos ir até N-1?
# 
# Essas perguntas levam ao tipo de pensamento voltado a deixar um algoritmo mais eficiente. Veja se você consegue melhorar o seu.

# In[5]:


import math

N = 98
primo = True

if N == 2 or N == 3:
    primo = True
elif N % 2 == 0 or N % 3 == 0:
    primo = False
else:
    for i in range(5, int(math.sqrt(N))+1, 6):
        if N % i == 0 or N % (i+2) == 0:
            primo = False
            break

if primo:
    print(f"{N} é um número primo.")
else:
    print(f"{N} não é um número primo.")


# ### 06 - Peso ideal 1
# O IMC (índice de massa corpórea) é um indicador de saúde mais bem aceito que o peso. Ele é calculado como:
# 
# $$ IMC = \dfrac{peso}{altura^2}$$
# 
# Segundo a OMS, valores *normais* são entre 18.5 e 24.9.
# 
# Sua tarefa é encontrar o ponto médio dessa faixa.

# In[6]:


limite_inferior = 18.5
limite_superior = 24.9
imc_ideal = (limite_inferior + limite_superior) / 2 ** 2

print("O IMC ideal é:", imc_ideal)

imc_ideal


# ### 07 - Peso ideal 2
# Recebendo um valor de altura, encontre o peso '*ideal*' dessa pessoa, que fornece o IMC encontrado acima

# In[7]:


altura = 1.70

# Seu código
limite_inferior = 18.5
limite_superior = 24.9
imc_ideal = (limite_inferior + limite_superior) / 2 ** 2
altura = 1.70

peso_ideal = imc_ideal * altura ** 2

print("O IMC ideal é:", imc_ideal)
print("O peso ideal para uma pessoa de altura", altura, "é:", peso_ideal)


# ### 08 - Peso ideal 3
# Dada uma lista contendo as alturas de pacientes, crie uma nova lista que contenha o peso '*ideal*' (que fornece o IMC calculado em **Peso ideal 1**) desses pacientes.

# In[8]:


limite_inferior = 18.5
limite_superior = 24.9
imc_ideal = (limite_inferior + limite_superior) / 2 ** 2

lista_alturas = [1.95, 2.05, 1.70, 1.65]
lista_peso_ideal = []

for altura in lista_alturas:
    peso_ideal = imc_ideal * altura ** 2
    lista_peso_ideal.append(peso_ideal)

print("A lista de pesos ideais é:", lista_peso_ideal)


# ### 09 - Peso ideal 4
# Dada uma lista de tuplas - cada elemento da lista é uma tupla contendo altura e peso de um paciente - crie uma nova lista com o IMC desses pacientes.

# In[9]:


altura_peso = [(1.80, 90), (1.65, 75), (1.91, 70)]

imc = []

for altura, peso in altura_peso:
    imc_paciente = peso / altura ** 2
    imc.append(imc_paciente)
    
print(imc)


# ### 10 - Peso ideal 5
# Dada uma lista de **listas** - cada elemento da lista é uma **lista** contendo altura e peso de um paciente, adicione mais um elemento à lista de cada paciente contendo o IMC do paciente. Verifique também se é 'baixo', 'normal' ou 'alto' segundo os padrões da OMS em que normal é entre 18.5 e 24.9.
# 
# Reflexão: por que no problema anterior temos que criar uma nova lista, e não podemos adicionar os dados de cada indivíduo à tupla?

# In[10]:


altura_peso = [[1.80, 90], [1.65, 75], [1.91, 70]]

for paciente in altura_peso:
    altura = paciente[0]
    peso = paciente[1]
    imc = peso / altura ** 2
    paciente.append(imc)
    if imc < 18.5:
        paciente.append('baixo')
    elif imc >= 18.5 and imc <= 24.9:
        paciente.append('normal')
    else:
        paciente.append('alto')

print(altura_peso)


# In[ ]:




