import math

#La velocidad de escape de un planeta se define como la mínima velocidad necesaria para salir de un planeta venciendo la gravedad.La velocidad de escape se calcula mediante la siguiente fórmula:



# Función para calcular la velocidad de escape
def calcular_velocidad_escape(g, r):
    # Usamos la fórmula Ve = sqrt(2 * g * r)
    velocidad_escape = math.sqrt(2 * g * r)
    return velocidad_escape

# Función principal del programa
def main():
    # Pedir que ingrese el radio del planeta en kilómetros
    radio_km = input("Ingrese el radio en kilómetros: ")
    # Convertimos el radio a tipo float y lo pasamos a metros
    radio_m = float(radio_km) * 1000

     # Pedir que ingrese la constante gravitacional
    g = input("Ingrese la constante g en m/s^2: ")
    # Convertimos la constante g a tipo float
    g = float(g)
    
    # Calcular la velocidad de escape llamando a la función calcular_velocidad_escape
    velocidad_escape = calcular_velocidad_escape(g, radio_m)
    
    # Mostramos el resultado con un mensaje claro
    print(f"La velocidad de escape es {velocidad_escape:.1f} [m/s]")

# Ejecutamos la función principal
if __name__ == "__main__":
    main()