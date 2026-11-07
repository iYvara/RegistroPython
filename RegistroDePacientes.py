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

# hola

while continuar == "s" or continuar == "S":
    print("==================")
    print("")
    print("DATOS DEL PACIENTE")
    print("")
    print("==================")

    codigoActual[contadordepacientes - 1] = GenerarCodigoPaciente(contadordepacientes)

    # NOMBRES
    print("Ingrese los nombres completos:")
    nombres[contadordepacientes - 1] = input()

    # APELLIDOS
    print("Ingrese los apellidos completos:")
    apellidos[contadordepacientes - 1] = input()

    # DNI
    print("Ingrese su DNI (8 dígitos):")
    dni[contadordepacientes - 1] = int(input())

    # FECHA
    fecha[contadordepacientes - 1] = datetime.now().strftime("%d/%m/%Y")

    # NIVEL DE EMERGENCIA
    print("¿Nivel de Emergencia? (1 al 5)")
    nivelEmergencia[contadordepacientes - 1] = int(input())

    # SOLICITUD
    print("¿Tipo de solicitud? (Ambulancia, Consulta, Medicamentos).")
    tipoSolicitud[contadordepacientes - 1] = str(input())