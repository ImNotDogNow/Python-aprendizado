# Curso Python #04 - Primeiros comandos em Python3

Excelente! Aprender **strings e formatação** é essencial para qualquer linguagem — e em Python, o trabalho com texto é **simples, poderoso e muito usado**.

Abaixo, você vai aprender **tudo sobre strings**, incluindo **operações, métodos, formatação e boas práticas**.

---

## 📌 O que é uma **string**?

Uma **string** é uma **sequência de caracteres** (texto).

```python
texto = "Olá, mundo!"
```

Você pode usar:

- Aspas simples: `'Python'`
    
- Aspas duplas: `"Python"`
    
- Aspas triplas: `'''Texto'''` ou `"""Texto"""` (para textos multi-linha)
    

---

## 🔤 Principais operações com strings

### ➕ Concatenação (juntar)

```python
nome = "Ana"
print("Olá, " + nome)
```

### 🔁 Repetição

```python
print("Ha" * 3)  # "HaHaHa"
```

### 📏 Tamanho da string

```python
len("Python")  # 6
```

### 🔍 Indexação e fatiamento (slicing)

```python
frase = "Programar"
print(frase[0])     # 'P'
print(frase[-1])    # 'r'
print(frase[0:4])   # 'Prog'
print(frase[4:])    # 'ramar'
print(frase[::-1])  # inverte a string
```

---

## 🧼 Métodos úteis de string

```python
texto = "  Python é TOP  "
```

|Método|O que faz|
|---|---|
|`texto.lower()`|Converte para minúsculas|
|`texto.upper()`|Converte para maiúsculas|
|`texto.strip()`|Remove espaços das pontas|
|`texto.replace("TOP", "10")`|Substitui "TOP" por "10"|
|`texto.split()`|Divide a string em uma lista|
|`" ".join(lista)`|Junta lista em string|
|`texto.startswith("Py")`|Verifica se começa com "Py"|
|`texto.endswith("TOP")`|Verifica se termina com "TOP"|
|`texto.find("é")`|Retorna posição do caractere|

---

## 🎯 Formatação de strings

### ✅ 1. `f-strings` (mais moderno e recomendado)

```python
nome = "Maria"
idade = 30
print(f"{nome} tem {idade} anos.")
```

### ✅ 2. `.format()`

```python
print("{} tem {} anos.".format(nome, idade))
```

### ✅ 3. `%` (forma antiga, mas ainda usada)

```python
print("%s tem %d anos." % (nome, idade))
```

---

## ✨ F-strings avançadas

```python
pi = 3.1415926535
print(f"Valor de pi: {pi:.2f}")         # 2 casas decimais
print(f"ID: {42:05}")                   # Preenchido com zeros: 00042
print(f"Nome: {nome:<10}")              # Alinhado à esquerda
print(f"Nome: {nome:>10}")              # À direita
```

---

## 🧪 Exemplo completo:

```python
nome = input("Digite seu nome: ").strip().title()
idade = int(input("Digite sua idade: "))
print(f"Bem-vindo, {nome}. Você tem {idade} anos.")
```

---

## 🛑 Cuidados comuns

|Problema|Correção|
|---|---|
|Esquecer de usar `str()`|`print("Idade: " + str(idade))`|
|Confundir índice com valor|`texto[2]` é caractere, não posição|
|Espaços indesejados|Use `.strip()`|

---

## 🧪 Quer praticar?

Aqui vão alguns desafios com strings:

1. Receber um nome completo e exibir:
    
    - Em maiúsculas, minúsculas
        
    - Quantas letras tem (sem espaços)
        
    - Primeira letra do nome
        
2. Verificar se uma palavra é **palíndromo**
    
3. Contar quantas vezes aparece uma letra numa frase
    
4. Criar um sistema de cadastro formatado com nome, CPF, idade, etc.
    
5. Formatador de mensagem de boas-vindas
