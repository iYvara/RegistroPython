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
    while True:
        print("Ingrese los nombres completos:")
        nombres[contadordepacientes - 1] = input()

        if nombres[contadordepacientes - 1] == "":
            print("Error: debe ingresar los nombres.")
        else:
            break

    # APELLIDOS
    while True:
        print("Ingrese los apellidos completos:")
        apellidos[contadordepacientes - 1] = input()

        if apellidos[contadordepacientes - 1] == "":
            print("Error: debe ingresar los apellidos.")
        else:
            break

    # DNI
    while True:
        print("Ingrese su DNI (8 dígitos):")
        dni[contadordepacientes - 1] = int(input())

        if dni[contadordepacientes - 1] < 10000000 or dni[contadordepacientes - 1] > 99999999:
            print("Error: el DNI debe tener 8 dígitos.")

        else:
            break

    # FECHA
    fecha[contadordepacientes - 1] = datetime.now().strftime("%d/%m/%Y")

    # NIVEL DE EMERGENCIA
    while True:
        print("¿Nivel de Emergencia? (1 al 5)")
        nivelEmergencia[contadordepacientes - 1] = int(input())
        if nivelEmergencia[contadordepacientes - 1] < 1 or nivelEmergencia[contadordepacientes - 1] > 5:
            print("Error: ingrese un nivel entre 1 y 5.")
        else:
            break

    # SOLICITUD
    while True:
        print("¿Tipo de solicitud? (Ambulancia, Consulta, Medicamentos).")
        tipoSolicitud[contadordepacientes - 1] = str(input())

        if tipoSolicitud[contadordepacientes - 1] == "":
            print("Ingrese correctamente el tipo de solicitud")
        else:
            break

    # CALCULAR PRIORIDAD
    prioridadFinal[contadordepacientes - 1] = CalcularPrioridad(nivelEmergencia[contadordepacientes - 1],tipoSolicitud)

    # MOSTRAR PACIENTE REGISTRADO
    print()
    print("============================")
    print("     SOLICITUD REGISTRADA")
    print("============================")

    print(f"Código: {codigoActual[contadordepacientes - 1]}")
    print(f"Fecha: {fecha[contadordepacientes - 1]}")
    print(f"Paciente: {nombres[contadordepacientes - 1]} {apellidos[contadordepacientes - 1]}")
    print(f"DNI: {dni[contadordepacientes - 1]}")
    print(f"Centro de Salud: {centroSalud}")
    print(f"Distrito: {distrito}")
    print(f"Tipo de Solicitud: {tipoSolicitud}")
    print(f"Prioridad: {prioridadFinal[contadordepacientes - 1]}")
    print(f"Descripción: {descripcion}")

    # ESTADO DE EMERGENCIA
    if nivelEmergencia[contadordepacientes - 1] == 1:
        print("Estado: Leve")
    elif nivelEmergencia[contadordepacientes - 1] == 2:
        print("Estado: Poco Leve")
    elif nivelEmergencia[contadordepacientes - 1] == 3:
        print("Estado: Severo")
    elif nivelEmergencia[contadordepacientes - 1] == 4:
        print("Estado: Muy Severo")
    elif nivelEmergencia[contadordepacientes - 1] == 5:
        print("Estado: Peligro")

    # REGISTRAR OTRO PACIENTE
    print()
    print("¿Desea registrar otro paciente? (S/N)")

    continuar = input().upper()

    if continuar == "S":
        contadordepacientes = contadordepacientes + 1

    if continuar == "N":
        break

    # BUSCAR PACIENTE
    while True:
        print()
    print("============================")
    print("       BUSCAR PACIENTE")
    print("============================")

    print("Ingrese el código del paciente:")
    codigoBusqueda = input()

    encontrado = False

    # RECORRER LOS PACIENTES
    for i in range(1, contadordepacientes + 1):
        if codigoBusqueda == codigoActual[i - 1]:
            encontrado = True

            print()
            print("============================")
            print("      PACIENTE ENCONTRADO")
            print("============================")

            print(f"Código: {codigoActual[i - 1]}")
            print(f"Fecha: {fecha[i - 1]}")
            print(f"Paciente: {nombres[i - 1]} {apellidos[i - 1]}")
            print(f"DNI: {dni[i - 1]}")
            print(f"Centro de Salud: {centroSalud}")
            print(f"Distrito: {distrito}")
            print(f"Tipo de Solicitud: {tipoSolicitud}")
            print(f"Nivel de Emergencia: {nivelEmergencia[i - 1]}")
            print(f"Prioridad: {prioridadFinal[i - 1]}")
            print(f"Descripción: {descripcion}")