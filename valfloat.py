print("=== Verificador de Número Flotante y Rango ===")
print("Este programa verifica si un número es de tipo flotante y, si se proporciona un rango, verifica si el número está dentro del rango.")
print("Si desea proporcionar un rango, ingréselo como una tupla o lista en el siguiente formato: (min, max)")
print("Por ejemplo: (0.0, 10.0) o [5.0, 15.0]\n")

# Pedir al usuario que ingrese un número
num = float(input("Ingrese un número: "))

# Pedir al usuario que ingrese el rango (opcional)
range_input = input("Ingrese el rango (opcional) como una tupla o lista (por ejemplo, (min, max)): ")

# Convertir el rango ingresado a una lista de números
try:
    range_list = eval(range_input)
except:
    range_list = None

# Verificar si num es un número flotante
variable = True
if not isinstance(num, float):
    variable = False

# Verificar si num está dentro del rango especificado por range_list
if range_list is not None:
    if isinstance(range_list, tuple):
        if range_list[0] >= range_list[-1]:
            raise ValueError("El rango proporcionado en forma de tupla no está ordenado de manera creciente")
        elif len(range_list) != 2:
            raise ValueError("El rango proporcionado en forma de tupla tiene más de dos elementos")
        elif num <= range_list[0] or num >= range_list[-1]:
            variable = False
    elif isinstance(range_list, list):
        if range_list[0] >= range_list[-1]:
            raise ValueError("El rango proporcionado en forma de lista no está ordenado de manera creciente")
        elif len(range_list) != 2:
            raise ValueError("El rango proporcionado en forma de lista tiene más de dos elementos")
        elif num < range_list[0] or num > range_list[-1]:
            variable = False
    else:
        raise TypeError("El segundo argumento no es del tipo correcto (debe ser una tupla o una lista)")

# Mostrar el resultado
if variable:
    print(f"El número {num} es de tipo flotante y está dentro del rango especificado.")
else:
    print(f"El número {num} no es de tipo flotante o está fuera del rango especificado.")

