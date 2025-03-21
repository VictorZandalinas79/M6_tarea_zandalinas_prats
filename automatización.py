# automatización.py
import sys
import time
from funciones.funciones_analisis import *
from funciones.funciones_backup import *
from funciones.funciones_limpieza import *
from funciones.funciones_consultas import *

def mostrar_menu():
    """
    Muestra el menú principal con las opciones disponibles.
    """
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Realizar análisis de datos")
    print("2. Realizar backup de la base de datos")
    print("3. Restaurar base de datos desde un backup")
    print("4. Limpiar y preprocesar datos")
    print("5. Ejecutar consultas y análisis de eficiencia")
    print("6. Salir")

def ejecutar_analisis():
    """
    Ejecuta las funciones de análisis de datos.
    """
    print("\n=== ANÁLISIS DE DATOS ===")
    consulta_efectividad_equipos()
    consulta_efectividad_tipos_lanzamiento()
    consulta_jugadores_mas_participaciones()
    consulta_efectividad_estrategias_defensa()
    consulta_distancias_recorridas()

def ejecutar_backup():
    """
    Ejecuta la función de backup.
    """
    print("\n=== BACKUP DE LA BASE DE DATOS ===")
    backup_file = realizar_backup()
    if backup_file:
        print(f"Backup realizado correctamente en: {backup_file}")
    else:
        print("Error al realizar el backup.")

def ejecutar_restauracion():
    """
    Ejecuta la función de restauración.
    """
    print("\n=== RESTAURACIÓN DE LA BASE DE DATOS ===")
    backup_file = input("Ingrese la ruta del archivo de backup: ")
    if restaurar_backup(backup_file):
        print("Base de datos restaurada correctamente.")
    else:
        print("Error al restaurar la base de datos.")

def ejecutar_limpieza_y_preprocesamiento():
    """
    Ejecuta la función de limpieza y preprocesamiento de datos.
    """
    print("\n=== LIMPIEZA Y PREPROCESAMIENTO DE DATOS ===")
    num_correcciones = limpiar_datos()
    num_transformaciones = transformar_datos()
    print(f"Total de correcciones aplicadas: {num_correcciones}")
    print(f"Total de transformaciones aplicadas: {num_transformaciones}")

def ejecutar_consultas_y_eficiencia():
    """
    Ejecuta las consultas y análisis de eficiencia.
    """
    print("\n=== CONSULTAS Y ANÁLISIS DE EFICIENCIA ===")
    query1 = "SELECT * FROM corners LIMIT 10;"  # Ejemplo de consulta
    explicar_plan_consulta(query1)
    medir_tiempo_consulta(query1)

def main():
    """
    Función principal del script.
    """
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == "1":
            ejecutar_analisis()
        elif opcion == "2":
            ejecutar_backup()
        elif opcion == "3":
            ejecutar_restauracion()
        elif opcion == "4":
            ejecutar_limpieza_y_preprocesamiento()
        elif opcion == "5":
            ejecutar_consultas_y_eficiencia()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        
        time.sleep(1)  # Pausa para mejorar la legibilidad

if __name__ == "__main__":
    main()