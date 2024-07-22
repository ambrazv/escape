# Solicitar datos al usuario
P = float(input("Introduce el precio de suscripción (P): "))
U = int(input("Introduce el número de usuarios (U): "))
GT = float(input("Introduce los gastos totales (GT): "))
U_anterior = float(input("Introduce las utilidades del año anterior (Uanterior): "))

# Advertencia sobre valores
if U_anterior == 0:
    print("Advertencia: Las utilidades del año anterior no pueden ser cero para calcular la razón.")
else:
    # Calcular utilidades actuales
    U_actuales = P * U - GT

    # Calcular la razón entre utilidades actuales y anteriores
    razon = U_actuales / U_anterior

    # Mostrar el resultado
    print(f"Las utilidades actuales del proyecto son: {U_actuales:.2f}")
    print(f"La razón entre las utilidades actuales y las del año anterior es: {razon:.2f}")