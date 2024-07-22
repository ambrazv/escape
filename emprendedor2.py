# Solicitar datos al usuario
P_normal = float(input("Introduce el precio de suscripción para usuarios normales (P): "))
P_premium = P_normal * 1.5
U_normal = int(input("Introduce el número de usuarios normales (Unormal): "))
U_premium = int(input("Introduce el número de usuarios premium (Upremium): "))
GT = float(input("Introduce los gastos totales (GT): "))

# Calcular utilidades
utilidades = (P_normal * U_normal) + (P_premium * U_premium) - GT

# Mostrar el resultado
print(f"Las utilidades del proyecto son: {utilidades:.2f}")