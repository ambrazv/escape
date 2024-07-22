# Solicitar datos 
P = float(input("Introduce el precio de suscripción (P): "))
U = int(input("Introduce el número de usuarios (U): "))
GT = float(input("Introduce los gastos totales (GT): "))

# Calcular utilidades
utilidades = P * U - GT

# Mostrar el resultado
print(f"Las utilidades del proyecto son: {utilidades:.2f}")
