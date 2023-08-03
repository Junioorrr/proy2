
print("=== Verificador de Número Complejo y Módulo en Rango ===")
print("Este programa verifica si un número es de tipo complejo y, si se proporciona un rango, verifica si el módulo del número está dentro de ese rango.")
print("Si desea proporcionar un rango, ingréselo como una tupla o lista en el siguiente formato: (min, max)")
print("Por ejemplo: (0.0, 10.0) o [5.0, 15.0]\n")

# Pedir al usuario que ingrese un número complejo
real_part = float(input("Ingrese la parte real del número complejo: "))
imag_part = float(input("Ingrese la parte imaginaria del número complejo: "))
num = complex(real_part, imag_part)

# Pedir al usuario que ingrese el rango (opcional)
range_input = input("Ingrese el rango (opcional) como una tupla o lista (por ejemplo, (min, max)): ")

# Convertir el rango ingresado a una lista de números
try:
    range_list = eval(range_input)
except:
    range_list = None

# Verificar si num es un número complejo
status = True
if not isinstance(num, complex):
    status = False

# Verificar si el módulo del número está dentro del rango especificado por range_list
if range_list is not None:
    complex_num_module = abs(num)
    if isinstance(range_list, tuple):
        if range_list[0] >= range_list[-1]:
            raise ValueError("El rango proporcionado no está ordenado de manera creciente")
        elif len(range_list) != 2:
            raise ValueError("El rango proporcionado tiene más de dos elementos")
        elif complex_num_module <= range_list[0] or complex_num_module >= range_list[-1]:
            status = False
    elif isinstance(range_list, list):
        if range_list[0] >= range_list[-1]:
            raise ValueError("El rango proporcionado no está ordenado de manera creciente")
        elif len(range_list) != 2:
            raise ValueError("El rango proporcionado tiene más de dos elementos")
        elif complex_num_module < range_list[0] or complex_num_module > range_list[1]:
            status = False
    else:
        raise TypeError("El segundo argumento no es del tipo correcto (debe ser una tupla o una lista)")

# Mostrar el resultado
if status:
    print(f"El número complejo {num} es de tipo complejo y el módulo está dentro del rango especificado.")
else:
    print(f"El número {num} no es de tipo complejo o el módulo no está dentro del rango especificado.")

