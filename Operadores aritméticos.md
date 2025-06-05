
## ➕ 1. Operadores Aritméticos Básicos

|Operador|Significado|Exemplo|Resultado|
|---|---|---|---|
|`+`|Soma|`2 + 3`|`5`|
|`-`|Subtração|`5 - 2`|`3`|
|`*`|Multiplicação|`3 * 4`|`12`|
|`/`|Divisão real|`10 / 2`|`5.0`|
|`//`|Divisão inteira|`10 // 3`|`3`|
|`%`|Módulo (resto)|`10 % 3`|`1`|
|`**`|Potência|`2 ** 3`|`8`|

### 🧠 Exemplo completo:

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

---

## 📌 2. Ordem de precedência

Python segue as **regras matemáticas tradicionais** (PEMDAS):

```
1. Parênteses           ()
2. Expoentes            **
3. Multiplicação        * /
4. Divisão inteira      //
5. Módulo               %
6. Soma/Subtração       + -
```

### 🧪 Exemplo:

```python
res = 2 + 3 * 4  # 2 + 12 = 14
res = (2 + 3) * 4  # 5 * 4 = 20
```

---

## 📥 3. Conversão de tipos

```python
x = "5"
y = int(x)  # agora y = 5 (int)
```

```python
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
print((nota1 + nota2) / 2)
```

---

## 🔀 4. Operadores combinados (atribuição com operação)

|Operador|Exemplo|Equivalente|
|---|---|---|
|`+=`|`x += 1`|`x = x + 1`|
|`-=`|`x -= 2`|`x = x - 2`|
|`*=`|`x *= 3`|`x = x * 3`|
|`/=`|`x /= 2`|`x = x / 2`|
|`**=`|`x **= 2`|`x = x ** 2`|

---

## 🎯 Aplicações práticas

### 🔸 Calcular média de 3 notas

```python
n1 = float(input())
n2 = float(input())
n3 = float(input())

media = (n1 + n2 + n3) / 3
print(f"Média: {media:.2f}")
```

---

### 🔸 Converter temperatura

```python
c = float(input("Temperatura em °C: "))
f = (c * 9/5) + 32
print(f"Em Fahrenheit: {f:.2f}")
```

---

## ✅ Boas práticas

- Sempre **converta input para `int` ou `float`** antes de operar
    
- Use `//` para evitar números decimais se quiser apenas inteiros
    
- Use `round(valor, casas)` para arredondar resultados
    
    ```python
    media = round((7.5 + 8.4 + 6.0) / 3, 1)
    ```
    

---

## ⚠️ Erros comuns

|Erro|Correção|
|---|---|
|Usar `/` esperando inteiro|Use `//`|
|Dividir por zero|Valide antes (`if b != 0`)|
|Esquecer conversão de tipo|`int(input())` ou `float(...)`|

---

## 🧪 Quer praticar?

Posso te passar desafios como:

1. Calcular área de um triângulo ou círculo
    
2. Simular uma calculadora com 4 operações
    
3. Mostrar o tempo total em segundos a partir de horas:minutos:segundos
    
4. Desconto aplicado a um preço
