# Pedir al usuario que ingrese una lista
input_list = input("Ingrese una lista de números (por ejemplo, [1, 2, 3]): ")

# Convertir la entrada a una lista de números
try:
    user_list = eval(input_list)
    if not isinstance(user_list, list):
        raise ValueError
except:
    print("La entrada no es válida. Por favor, ingrese la lista de números en el formato correcto.")
    exit()

# Pedir al usuario que ingrese el valor opcional 'var'
input_var = input("Ingrese el valor opcional 'var' como una lista o un número entero (o presione Enter para omitir): ")

# Convertir la entrada de 'var' a la forma deseada (lista o número entero)
if input_var:
    try:
        var = eval(input_var)
    except:
        print("La entrada no es válida para 'var'. Debe ser una lista o un número entero.")
        exit()
else:
    var = None

# Pedir al usuario que ingrese el valor opcional 'string'
input_string = input("Ingrese el valor opcional 'string' como 'value' o 'len' (o presione Enter para omitir): ")

# Verificar si 'string' es válido (si se proporciona)
if input_string:
    if input_string != "value" and input_string != "len":
        print("El valor de 'string' debe ser 'value' o 'len'.")
        exit()
    string = input_string
else:
    string = None

# Verificación de los datos ingresados
status = True

# Verificar si user_list es una lista
if not isinstance(user_list, list):
    status = False

# Verificar si se proporcionaron var y string (opcional)
if var is not None or string is not None:
    if string == "value":
        if isinstance(var, list):
            if not var == user_list:
                status = False
        else:
            status = False
    elif string == "len":
        if isinstance(var, int):
            var = str(var)
            if not len(user_list) == len(var):
                status = False
        else:
            status = False
    else:
        if not isinstance(var, list) or not isinstance(var, int):
            print("El segundo argumento no es de tipo lista o entero.")
            exit()
        else:
            print("El tercer argumento no es 'value' o 'len'.")
            exit()

# Mostrar el resultado
if status:
    print("La lista es válida y las condiciones se cumplen.")
else:
    print("La lista no es válida o no cumple con las condiciones especificadas.")
