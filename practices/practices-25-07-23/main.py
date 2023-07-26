
# Ejercicio:

# Una empresa está organizando la agenda de eventos para el mes de agosto. Por lo tanto requiere un programa que:
#   Permita registrar a los participantes de los eventos de agosto pidiendo: documento, nombre, edad y cargo.
#   Permita registrar los eventos  pidiendo: nombre del evento, locación y día del mes
#   Permita quitar del registro a los participantes .
#   Permita eliminar y/o modificar eventos.

# Para participar los empleados deben cancelar un aporte de 50.000 COP. Por lo tanto el programa también debe:
#   Saber cuantos empleados no han cancelado aún el aporte y cuanto dinero suma la deuda.
#   Saber cuales empleados (listarlos) no han cancelado.
#   No permitir quitar del registro a participantes que ya hayan pagado, pues no se aceptan devoluciones
#   Marcar eventos ya realizados.
#   No permitir eliminar o modificar eventos ya realizados.

# Aspectos a tener en cuenta: 
#   La estructura a utilizar es libre, solo se pide que sea ordenada y coherente. 
#   Todo debe ser dentro de un menú que se repite para no perder la información y al presionar 
#   la opción de salida se debe pedir confirmación de la misma. 
#   Se deben manejar la excepciones


from funciones import menu_text, operation_options




Agendas = {}


while True:
    try:
        menu_text()
        opc = int(input("Ingresa una opcion: "))
        operation_options(opc,Agendas)
    except ValueError:
        print("Error valor no numerico")