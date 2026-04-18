# ==========================================
# EJERCICIO 1: Caja del Kiosco
# ==========================================
print("--- EJERCICIO 1: CAJA DEL KIOSCO ---")

# Validar nombre del cliente (solo letras y no vacío)
nombre = input("Cliente: ")
while not nombre.isalpha():
    print("Error: El nombre debe contener solo letras y no estar vacío.")
    nombre = input("Cliente: ")

# Validar cantidad de productos (entero positivo)
cant_str = input("Cantidad de productos: ")
while not cant_str.isdigit() or int(cant_str) <= 0:
    print("Error: Ingrese un número entero mayor a 0.")
    cant_str = input("Cantidad de productos: ")

cant_productos = int(cant_str)
total_sin_desc = 0
total_con_desc = 0

for i in range(1, cant_productos + 1):
    print(f"\nProducto {i}")
    
    # Validar precio
    precio_str = input("Precio: ")
    while not precio_str.isdigit():
        print("Error: Ingrese un precio válido.")
        precio_str = input("Precio: ")
    
    precio = int(precio_str)
    total_sin_desc += precio
    
    # Validar descuento S/N
    tiene_desc = input("¿Tiene descuento? (S/N): ").lower()
    while tiene_desc not in ['s', 'n']:
        print("Error: Ingrese 'S' o 'N'.")
        tiene_desc = input("¿Tiene descuento? (S/N): ").lower()
    
    if tiene_desc == 's':
        precio_final = precio * 0.90  # Aplicar 10% de descuento
    else:
        precio_final = precio
        
    total_con_desc += precio_final

ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cant_productos

print("-" * 30)
print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
print("-" * 30)


# ==========================================
# EJERCICIO 2: Acceso al Campus y Menú Seguro
# ==========================================
print("\n--- EJERCICIO 2: ACCESO AL CAMPUS ---")

USER_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"
intentos = 1
acceso = False

while intentos <= 3:
    print(f"Intento {intentos}/3")
    user = input("Usuario: ")
    clave = input("Clave: ")
    
    if user == USER_CORRECTO and clave == CLAVE_CORRECTA:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if not acceso:
    print("Cuenta bloqueada.")
else:
    # Menú repetitivo
    opcion = ""
    while opcion != "4":
        print("\n1) Ver estado de inscripción")
        print("2) Cambiar clave")
        print("3) Mensaje motivacional")
        print("4) Salir")
        
        opcion = input("Opción: ")
        
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue
        
        if opcion == "1":
            print("Estado: Inscripto")
        elif opcion == "2":
            nueva_clave = input("Nueva clave: ")
            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")
            
            confirmacion = input("Confirme la clave: ")
            if nueva_clave == confirmacion:
                CLAVE_CORRECTA = nueva_clave
                print("Clave cambiada con éxito.")
            else:
                print("Las claves no coinciden.")
        elif opcion == "3":
            print("Mensaje: 'El éxito es la suma de pequeños esfuerzos repetidos día tras día'.")
        elif opcion == "4":
            print("Saliendo del sistema...")
        else:
            print("Error: opción fuera de rango.")


# ==========================================
# EJERCICIO 3: Agenda de Turnos (Sin Listas)
# ==========================================
print("\n--- EJERCICIO 3: AGENDA DE TURNOS ---")

# Variables para Lunes (4 cupos)
lunes1 = ""; lunes2 = ""; lunes3 = ""; lunes4 = ""
# Variables para Martes (3 cupos)
martes1 = ""; martes2 = ""; martes3 = ""

operador = input("Nombre del operador: ")
while not operador.isalpha():
    operador = input("Error. Nombre del operador: ")

menu_agenda = ""
while menu_agenda != "5":
    print("\n--- MENÚ AGENDA ---")
    print("1. Reservar turno\n2. Cancelar turno\n3. Ver agenda del día\n4. Ver resumen general\n5. Cerrar sistema")
    menu_agenda = input("Elija una opción: ")

    if menu_agenda == "1":
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha(): paciente = input("Error. Nombre paciente: ")

        if dia == "1":
            if paciente in (lunes1, lunes2, lunes3, lunes4): print("Error: Paciente ya tiene turno.")
            elif lunes1 == "": lunes1 = paciente; print("Reservado en Turno 1")
            elif lunes2 == "": lunes2 = paciente; print("Reservado en Turno 2")
            elif lunes3 == "": lunes3 = paciente; print("Reservado en Turno 3")
            elif lunes4 == "": lunes4 = paciente; print("Reservado en Turno 4")
            else: print("Día completo.")
        elif dia == "2":
            if paciente in (martes1, martes2, martes3): print("Error: Paciente ya tiene turno.")
            elif martes1 == "": martes1 = paciente; print("Reservado en Turno 1")
            elif martes2 == "": martes2 = paciente; print("Reservado en Turno 2")
            elif martes3 == "": martes3 = paciente; print("Reservado en Turno 3")
            else: print("Día completo.")

    elif menu_agenda == "2":
        dia = input("Día para cancelar (1 o 2): ")
        paciente = input("Nombre del paciente a cancelar: ")
        if dia == "1":
            if lunes1 == paciente: lunes1 = ""
            elif lunes2 == paciente: lunes2 = ""
            elif lunes3 == paciente: lunes3 = ""
            elif lunes4 == paciente: lunes4 = ""
            else: print("No se encontró al paciente.")
        elif dia == "2":
            if martes1 == paciente: martes1 = ""
            elif martes2 == paciente: martes2 = ""
            elif martes3 == paciente: martes3 = ""
            else: print("No se encontró al paciente.")

    elif menu_agenda == "3":
        dia = input("Ver agenda de (1=Lunes, 2=Martes): ")
        if dia == "1":
            print(f"1: {lunes1 or '(libre)'}, 2: {lunes2 or '(libre)'}, 3: {lunes3 or '(libre)'}, 4: {lunes4 or '(libre)'}")
        elif dia == "2":
            print(f"1: {martes1 or '(libre)'}, 2: {martes2 or '(libre)'}, 3: {martes3 or '(libre)'}")

    elif menu_agenda == "4":
        occ_lunes = (lunes1!="") + (lunes2!="") + (lunes3!="") + (lunes4!="")
        occ_martes = (martes1!="") + (martes2!="") + (martes3!="")
        print(f"Lunes: {occ_lunes} ocupados, {4-occ_lunes} libres.")
        print(f"Martes: {occ_martes} ocupados, {3-occ_martes} libres.")


# ==========================================
# EJERCICIO 4: Escape Room: La Bóveda
# ==========================================
print("\n--- EJERCICIO 4: LA BÓVEDA ---")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidos = 0

nombre_agente = input("Nombre del agente: ")
while not nombre_agente.isalpha():
    nombre_agente = input("Error. Solo letras: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"\nEstado: Energía {energia} | Tiempo {tiempo} | Cerraduras {cerraduras_abiertas} | Alarma {'ON' if alarma else 'OFF'}")
    print("1. Forzar cerradura (-20E, -2T)\n2. Hackear panel (-10E, -3T)\n3. Descansar (+15E, -1T)")
    
    opc = input("Acción: ")
    if not opc.isdigit(): continue
    
    if opc == "1":
        forzar_seguidos += 1
        if forzar_seguidos == 3:
            energia -= 20; tiempo -= 2; alarma = True
            print("¡La cerradura se trabó! Alarma activada.")
        else:
            if energia < 40:
                n = input("Riesgo! Elija 1-3: ")
                if n == "3": alarma = True
            if not alarma:
                cerraduras_abiertas += 1
                energia -= 20; tiempo -= 2
                print("Cerradura abierta.")
    
    elif opc == "2":
        forzar_seguidos = 0
        energia -= 10; tiempo -= 3
        for _ in range(4):
            codigo_parcial += "A"
            print(f"Hackeando... {codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Hackeo exitoso! Cerradura abierta.")
            
    elif opc == "3":
        forzar_seguidos = 0
        tiempo -= 1
        recupera = 15
        if alarma: recupera -= 10
        energia = min(100, energia + recupera)
        print(f"Descansando. Energía actual: {energia}")

if cerraduras_abiertas == 3: print("¡VICTORIA!")
else: print("DERROTA: Bóveda bloqueada o sin recursos.")


# ==========================================
# EJERCICIO 5: La Arena del Gladiador
# ==========================================
print("\n--- EJERCICIO 5: LA ARENA ---")

nombre_g = input("Nombre del Gladiador: ")
while not nombre_g.isalpha() or nombre_g == "":
    print("Error: Solo se permiten letras.")
    nombre_g = input("Nombre del Gladiador: ")

hp_g = 100
hp_e = 100
pociones = 3
ataque_pesado = 15
ataque_enemigo = 12

while hp_g > 0 and hp_e > 0:
    print(f"\n{nombre_g} (HP: {hp_g}) vs Enemigo (HP: {hp_e}) | Pociones: {pociones}")
    print("1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")
    
    opc = input("Opción: ")
    while not opc.isdigit() or opc not in ["1", "2", "3"]:
        opc = input("Error. Elija 1, 2 o 3: ")
    
    if opc == "1":
        danio = float(ataque_pesado)
        if hp_e < 20:
            danio *= 1.5
            print("¡GOLPE CRÍTICO!")
        hp_e -= int(danio)
        print(f"Atacaste por {danio} de daño.")
    
    elif opc == "2":
        print(">> ¡Inicias una ráfaga!")
        for _ in range(3):
            hp_e -= 5
            print("> Golpe conectado por 5 de daño")
            
    elif opc == "3":
        if pociones > 0:
            hp_g += 30
            pociones -= 1
            print("Te has curado.")
        else:
            print("¡No quedan pociones!")

    if hp_e > 0:
        hp_g -= ataque_enemigo
        print(f"¡El enemigo te atacó por {ataque_enemigo}!")

if hp_g > 0: print(f"¡VICTORIA! {nombre_g} ha ganado.")
else: print("DERROTA. Has caído.")
