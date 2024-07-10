import geopy.distance
from geopy.geocoders import Nominatim

def obtener_coordenadas(ciudad):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(ciudad)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

def calcular_distancia(ciudad_origen, ciudad_destino):
    coord_origen = obtener_coordenadas(ciudad_origen)
    coord_destino = obtener_coordenadas(ciudad_destino)
    if coord_origen and coord_destino:
        distancia_km = geopy.distance.distance(coord_origen, coord_destino).km
        distancia_millas = geopy.distance.distance(coord_origen, coord_destino).miles
        return distancia_km, distancia_millas
    else:
        return None, None

def calcular_duracion(distancia_km, medio_transporte):
    if medio_transporte == "auto":
        velocidad = 80  # km/h
    elif medio_transporte == "avión":
        velocidad = 800  # km/h
    else:
        velocidad = 5  # km/h para caminar

    duracion_horas = distancia_km / velocidad
    return duracion_horas

def mostrar_narrativa(ciudad_origen, ciudad_destino, distancia_km, distancia_millas, duracion_horas, medio_transporte):
    print(f"\nNarrativa del viaje:")
    print(f"Origen: {ciudad_origen}")
    print(f"Destino: {ciudad_destino}")
    print(f"Distancia: {distancia_km:.2f} km / {distancia_millas:.2f} millas")
    print(f"Duración del viaje en {medio_transporte}: {duracion_horas:.2f} horas")

def main():
    while True:
        ciudad_origen = input("Ingrese la Ciudad de Origen: ")
        ciudad_destino = input("Ingrese la Ciudad de Destino: ")
        medio_transporte = input("Ingrese el medio de transporte (auto, avión, caminar): ").lower()

        if medio_transporte not in ["auto", "avión", "caminar"]:
            print("Medio de transporte no válido. Intente de nuevo.")
            continue

        distancia_km, distancia_millas = calcular_distancia(ciudad_origen, ciudad_destino)
        if distancia_km is None:
            print("No se pudo calcular la distancia. Verifique las ciudades e intente de nuevo.")
            continue

        duracion_horas = calcular_duracion(distancia_km, medio_transporte)
        mostrar_narrativa(ciudad_origen, ciudad_destino, distancia_km, distancia_millas, duracion_horas, medio_transporte)

        salir = input("¿Desea salir? (s para salir, cualquier otra tecla para continuar): ").lower()
        if salir == 's':
            break

if __name__ == "__main__":
    main()

