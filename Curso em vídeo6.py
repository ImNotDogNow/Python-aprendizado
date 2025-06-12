# Exercícios de conversões de temperatura º Celsius, Fahrenheit e Kelvin
c = float(input("Digite uma temperatura em ºCelsius: "))
k = c + 273.15
f = c * 1.8 + 32
print(f"A Temperatura indicada foi {c}ºC, em Kelvin é {k}ºK e em Fahrenheit é {f}ºF")
print(f"Você saiba que o Celsius é usada na maioria dos países?!")

# Ex. 2
f = float(input("Insira uma temperatura em ºFahrenheit: ")) 
k = (f - 32) / 1.8 + 273.15
c = (f - 32) / 1.8
print(f"A Temperatura indicada foi {f}ºF, em Kelvin é {k}ºK e em Celsius é {c}ºC")
print(f"Você sabia que nos EUA é medida a temperatura em ºF?!")

# Ex. 3
k = float(input("Insira uma temperatura em ºKelvin: ")) 
f = (k - 273.15) * 1.8 + 32
c = k- 273.15
print(f"A Temperatura indicada foi {k}ºK, em Fahrenheit é {f}ºF e em Celsius é {c}ºC")
print(f"Você sabia que o ºK é muito utilizado na ciência?!")
