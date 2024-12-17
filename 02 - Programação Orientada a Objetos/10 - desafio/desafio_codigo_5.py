Class ConversorTemperatura:
    def celsius_para_fahrenheit(self, celsius):
        return celsius*1.8+32

# Entrada do usuário
celsius = float(input())

# TODO: Crie uma instância do conversor:
conversor = ConversorTemperatura()

fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)