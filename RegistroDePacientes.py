from datetime import datetime
import os

ARCHIVO = "pacientes.txt"

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
opcion = ""

# LISTAS con datos:

codigoActual = [""] * 100
nombres = [""] * 100
apellidos = [""] * 100
dni = [""] * 100
fecha = [""] * 100
nivelEmergencia = [0] * 100
prioridadFinal = [0] * 100

distrito = "El Agustino"
centroSalud = "Hospital Nacional Unanue"
tipoSolicitud = [""] * 100
descripcion = [""] * 100
tiposValidos = ["Ambulancia", "Consulta", "Medicamentos"]

# RF08: guardar solicitudes
def GuardarPacientes(cantidad):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for k in range(cantidad):
            campos = [
                codigoActual[k],
                nombres[k],
                apellidos[k],
                str(dni[k]),
                fecha[k],
                str(nivelEmergencia[k]),
                str(prioridadFinal[k]),
                tipoSolicitud[k],
                descripcion[k]
            ]
            campos = [c.replace("|", "/") for c in campos]
            f.write("|".join(campos) + "\n")

# RF09: recuperar solicitudes
def CargarPacientes():
    cantidad = 0
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea == "" or cantidad >= 100:
                    continue
                datos = linea.split("|")
                if len(datos) != 9:
                    continue
                codigoActual[cantidad] = datos[0]
                nombres[cantidad] = datos[1]
                apellidos[cantidad] = datos[2]
                dni[cantidad] = datos[3]
                fecha[cantidad] = datos[4]
                nivelEmergencia[cantidad] = int(datos[5])
                prioridadFinal[cantidad] = int(datos[6])
                tipoSolicitud[cantidad] = datos[7]
                descripcion[cantidad] = datos[8]
                cantidad = cantidad + 1
    return cantidad


# hola

contadordepacientes = CargarPacientes()

while True:
    print()
    print("============================")
    print("      MENÚ PRINCIPAL")
    print("============================")
    print("1. Registrar solicitud")
    print("2. Buscar solicitud")
    print("3. Mostrar solicitudes")
    print("4. Mostrar solicitudes por prioridad")
    print("0. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":

        while True:
            if contadordepacientes >= 100:
                print("Error: se alcanzó el máximo de solicitudes.")
                break

            contadordepacientes = contadordepacientes + 1

            print("==================")
            print("")
            print("DATOS DEL PACIENTE")
            print("")
            print("==================")

            codigoActual[contadordepacientes - 1] = GenerarCodigoPaciente(contadordepacientes)

            # NOMBRES
            while True:
                print("Ingrese los nombres completos:")
                nombres[contadordepacientes - 1] = input().strip()

                if nombres[contadordepacientes - 1] == "":
                    print("Error: debe ingresar los nombres.")
                else:
                    break

            # APELLIDOS
            while True:
                print("Ingrese los apellidos completos:")
                apellidos[contadordepacientes - 1] = input().strip()

                if apellidos[contadordepacientes - 1] == "":
                    print("Error: debe ingresar los apellidos.")
                else:
                    break

            # DNI
            while True:
                print("Ingrese su DNI (8 dígitos):")
                textoDni = input().strip()

                if textoDni.isdigit() and len(textoDni) == 8:
                    dni[contadordepacientes - 1] = textoDni
                    break
                print("Error: el DNI debe tener 8 dígitos.")

            # FECHA
            fecha[contadordepacientes - 1] = datetime.now().strftime("%d/%m/%Y")

            # NIVEL DE EMERGENCIA
            while True:
                print("¿Nivel de Emergencia? (1 al 5)")
                textoNivel = input().strip()

                if textoNivel.isdigit() and 1 <= int(textoNivel) <= 5:
                    nivelEmergencia[contadordepacientes - 1] = int(textoNivel)
                    break
                print("Error: ingrese un nivel entre 1 y 5.")

            # SOLICITUD
            while True:
                print("¿Tipo de solicitud? (Ambulancia, Consulta, Medicamentos).")
                tipoSolicitud[contadordepacientes - 1] = input().strip().capitalize()

                if tipoSolicitud[contadordepacientes - 1] in tiposValidos:
                    break
                print("Error: ingrese Ambulancia, Consulta o Medicamentos.")

            # DESCRIPCIÓN
            while True:
                print("Ingrese la descripción:")
                descripcion[contadordepacientes - 1] = input().strip()

                if descripcion[contadordepacientes - 1] == "":
                    print("Error: debe ingresar la descripción.")
                else:
                    break

            # CALCULAR PRIORIDAD
            prioridadFinal[contadordepacientes - 1] = CalcularPrioridad(nivelEmergencia[contadordepacientes - 1], tipoSolicitud[contadordepacientes - 1])

            # GUARDAR EN ARCHIVO
            GuardarPacientes(contadordepacientes)

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
            print(f"Tipo de Solicitud: {tipoSolicitud[contadordepacientes - 1]}")
            print(f"Prioridad: {prioridadFinal[contadordepacientes - 1]}")
            print(f"Descripción: {descripcion[contadordepacientes - 1]}")

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

            while continuar != "S" and continuar != "N":
                print("Error: ingrese S o N.")
                continuar = input().upper()

            if continuar == "N":
                break

    elif opcion == "2":

        # BUSCAR PACIENTE
        if contadordepacientes == 0:
            print("No hay solicitudes registradas.")
        else:
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
                        print(f"Tipo de Solicitud: {tipoSolicitud[i - 1]}")
                        print(f"Nivel de Emergencia: {nivelEmergencia[i - 1]}")
                        print(f"Prioridad: {prioridadFinal[i - 1]}")
                        print(f"Descripción: {descripcion[i - 1]}")

                if encontrado == False:
                    print("Error: no se encontró ningún paciente con ese código.")

                print()
                print("¿Desea buscar otro paciente? (S/N)")

                decision = input().upper()

                if decision == "N":
                    break

    elif opcion == "3":
        MostrarSolicitudes(contadordepacientes, False)

    elif opcion == "4":
        MostrarSolicitudes(contadordepacientes, True)

    elif opcion == "0":
        print("Hasta luego.")
        break

    else:
        print("Opción no válida.")