import datetime

def GenerarCodigoPaciente(contador):
    numeroTexto = str(contador)
    while len(numeroTexto) < 4:
        numeroTexto = "0" + numeroTexto
    return "PAC-" + numeroTexto

def CalcularPrioridad(nivelEmergencia, tipoSolicitud):
    prioridad = nivelEmergencia * 2
    tipoSolicitud = tipoSolicitud.capitalize()
    if tipoSolicitud == "Ambulancia":
        prioridad = prioridad + 3
    elif tipoSolicitud == "Consulta":
        prioridad = prioridad + 1
    elif tipoSolicitud == "Medicamentos":
        prioridad = prioridad + 2
    return prioridad

# VARIABLES:

contadordepacientes = 0
i = 0
encontrado = False
continuar = "s"
decision = ""
codigoBusqueda = ""

# LISTAS con datos:

codigoActual = [""] * 100
nombres = [""] * 100
apellidos = [""] * 100
dni = [0] * 100
fecha = [""] * 100
nivelEmergencia = [0] * 100
prioridadFinal = [0] * 100

distrito = "El Agustino"
centroSalud = "Hospital Nacional Unanue"
tipoSolicitud = (str(input()))
descripcion = (str(input()))

