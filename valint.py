print("=== Verificador de Número Entero y Rango ===")
print("Este programa verifica si un número es de tipo entero y, si se proporciona un rango, verifica si el número está dentro de ese rango.")
print("Si desea proporcionar un rango, ingréselo como una tupla o lista en el siguiente formato: (min, max)")
print("Por ejemplo: (0, 10) o [5, 15]\n")

# Pedir al usuario que ingrese un número entero
num = int(input("Ingrese un número entero: "))

# Pedir al usuario que ingrese el rango (opcional)
range_input = input("Ingrese el rango (opcional) como una tupla o lista (por ejemplo, (min, max)): ")

# Convertir el rango ingresado a una lista de números
try:
    range_list = eval(range_input) if range_input else None
except:
    range_list = None

# Verificar si num es un número entero
variable = True
if not isinstance(num, int):
    variable = False
    print("El número no es de tipo entero.")

# Verificar si num está dentro del rango especificado por range_list
if range_list is not None:
    if isinstance(range_list, tuple):
        print("Se ha proporcionado un rango en formato de tupla.")
        if range_list[0] >= range_list[-1]:
            raise ValueError("El rango proporcionado no está ordenado de manera creciente")
        elif len(range_list) != 2:
            raise ValueError("El rango proporcionado tiene más de dos elementos")
        elif num <= range_list[0] or num >= range_list[-1]:
            variable = False
    elif isinstance(range_list, list):
        print("Se ha proporcionado un rango en formato de lista.")
        if range_list[0] >= range_list[-1]:
            raise ValueError("El rango proporcionado no está ordenado de manera creciente")
        elif len(range_list) != 2:
            raise ValueError("El rango proporcionado tiene más de dos elementos")
        elif num < range_list[0] or num > range_list[1]:
            variable = False
    else:
        raise TypeError("El segundo argumento no es del tipo correcto (debe ser una tupla o una lista)")

# Mostrar el resultado
if variable:
    print(f"El número {num} es de tipo entero.")
    if range_list is not None:
        print(f"El número {num} está dentro del rango especificado.")
    else:
        print("No se proporcionó un rango, por lo que no se realizó la verificación.")
else:
    print(f"El número {num} no es de tipo entero o está fuera del rango especificado.")
