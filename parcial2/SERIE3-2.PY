import sys

def calc_suma(valores):
    suma = sum(valores)
    return suma

def calc_promedio(valores):
    promedio = sum(valores) / len(valores)
    return promedio

if __name__ == "__main__":
    valores = sys.argv[1].split(",")
    valores = [int(valor) for valor in valores]
    
    suma = calc_suma(valores)
    promedio = calc_promedio(valores)
    
    print("La suma es", suma)
    print("El promedio es", promedio)