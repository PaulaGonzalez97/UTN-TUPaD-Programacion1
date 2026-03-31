#TP integrador – Repetitivas- Condicionales y Secuenciales.

#Ejercicio 1— “Caja del Kiosco”

nombre = str(input("Ingrese su nombre: "))

while not nombre.isalpha():
    print("Debes ingresar tu nombre correctamente.")
    nombre = input("Ingrese su nombre: ")

cantidad_prod = input("Ingrese la cantidad de productos que desee comprar: ")

while not cantidad_prod.isdigit() or int(cantidad_prod) <= 0:
    print("Debes ingresar un número entero positivo.")
    cantidad_prod = int(input("Ingrese la cantidad de productos que desee comprar: "))
cantidad_prod = int(cantidad_prod)

total_con_descuento = 0
total_sin_descuento = 0

for i in range (cantidad_prod):
    print(f"Producto {i + 1}:")
    precio = input("Ingrese el precio del producto: ")
    while not precio.isdigit():
        print("Debes ingresar un número correcto.")
        precio = input("Debes ingresar un número correcto.")
    precio = int(precio)

    total_sin_descuento += precio

    descuento = input("Tiene descuento? S/N: ").lower()
    while descuento != "s" and descuento != "n":
        print("Incorrecto, debes ingresar S o N. ")
        descuento = input("Tiene descuento? S/N: ").lower()

    if descuento == "s":
        precio_final = precio * 0.9
    else:
        precio_final = precio

    total_con_descuento += precio_final

    ahorro = total_sin_descuento - total_con_descuento
    promedio = total_con_descuento / cantidad_prod

    print(f"Cliente {nombre}")
    print(f"Cantidad de productos: {cantidad_prod}")
    print("Producto ",i+1,"- Precio: ",precio,"- Descuento (S/N): ",descuento)
    print("Total sin descuento: ",total_sin_descuento)
    print("Total con descuento: ",total_con_descuento)
    print("Ahorro: ",ahorro)
    print(f"Promedio por producto: {promedio:.2f}")
    print("----------------------------")




# Ejercicio 2 — “Acceso al Campus y Menú Seguro” Objetivo: Login con intentos + menú de acciones con validación estricta. Requisitos


usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0

for intentos in range (3):
    usuario = str(input("Ingrese su usuario: "))
    clave = str(input("Ingrese su clave: "))
    print(f"Intento {intentos+1}/3")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        while True:
            print("1. Estado de inscripción.  2. Cambiar clave.  3. Mensaje. 4. Salir.")
            opcion = input("Seleccione una opción (1-4): ")

            while not opcion.isdigit() or int(opcion) <1 or int(opcion) > 4: 
                print("Error: ingrese un número valido.")  
                opcion = input("Seleccione una opción (1-4): ")                       
            opcion = int(opcion)

            if opcion == 1:
                print("Inscripto")
            elif opcion == 2:
                nueva_clave = input("Ingrese la nueva clave: ")
                while len(nueva_clave) < 6:
                    print("Error: minimo 6 caracteres.")
                    nueva_clave = input("Ingrese la nueva clave: ")
                confirmacion = input("Confirme la nueva clave: ")
                while confirmacion != nueva_clave:
                    print("Las claves no coinciden. Intente nuevamente.")
                    confirmacion = input("Confirme la nueva clave: ")
                print("Clave cambiada correctamente.")
            elif opcion ==3:
                frase = "La programación no se trata de lo que sabes, sino de lo que puedes descubrir."
                print(frase)
            elif opcion == 4:
                print("Salida exitosa.")
                break
        break
else:
    print("Cuenta bloqueada.")


# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
    

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""
opcion = 0

operador = str(input("Ingrese su nombre: "))

while not operador.replace(" ", "").isalpha():
    print("Error. Ingrese su nombre nuevamente: ")
    operador = str(input("Ingrese su nombre: "))
print(f"Bienvenido/a {operador}!")

while opcion != 5:
    opcion = int(input("Elija una opción del menu:\n1. Reservar turno.\n2. Cancelar turno.\n3. Ver agenda del dia.\n4. Ver resumen general.\n5. Salir.\n" ))
    if opcion == 1:
        elegir_dia = int(input("Elija el dia que desea reservar el turno:\n1. Lunes\n2. Martes\n"))
        paciente = input("Ingrese el nombre del paciente: ")
        while not paciente.replace(" ", "").isalpha():
            print("Error. Ingrese el nombre nuevamente: ")
            paciente = input("Ingrese el nombre del paciente: ")
        
        if elegir_dia == 1:
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Ese paciente ya tiene turno.")
            else:
                if lunes1 == "":
                    lunes1 = paciente
                    print("Turno reservado.")
                elif lunes2 == "":
                    lunes2 = paciente
                    print("Turno reservado.")
                elif lunes3 == "":
                    lunes3 = paciente
                    print("Turno reservado.")
                elif lunes4 == "":
                    lunes4 = paciente
                    print("Turno reservado.")
                else: 
                    print("No hay cupos disponibles.")        
        elif elegir_dia == 2:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Ese paciente ya tiene turno.")
            else:
                if martes1 == "":
                    martes1 = paciente
                    print("Turno reservado.")
                elif martes2 == "":
                    martes2 = paciente
                    print("Turno reservado.")
                elif martes3 == "":
                    martes3 = paciente
                    print("Turno reservado.")
                else: 
                    print("No hay cupos disponibles.")    
    elif opcion == 2:
        elegir_dia = int(input("Elija el dia que desea cancelar el turno:\n1. Lunes\n2. Martes\n"))
        paciente = input("Ingrese el nombre del paciente que desea cancelar el turno: ")
        while not paciente.replace(" ", "").isalpha():
            print("Error. Ingrese el nombre nuevamente: ")
            paciente = input("Ingrese el nombre del paciente que desea cancelar el turno: ")
        if elegir_dia == 1:
            if paciente == lunes1:
                lunes1 = ""
                print("Turno cancelado.")
            elif paciente == lunes2:
                lunes2 = ""
                print("Turno cancelado.")
            elif paciente == lunes3:
                lunes3 = ""
                print("Turno cancelado.")
            elif paciente == lunes4:
                lunes4 = ""
                print("Turno cancelado.")
            else:
                print("Ese paciente no tiene turno.")
        elif elegir_dia == 2:
            if paciente == martes1:
                martes1 = ""
                print("Turno cancelado.")
            elif paciente == martes2:
                martes2 = ""
                print("Turno cancelado.")
            elif paciente == martes3:
                martes3 = ""
                print("Turno cancelado.")
            else:
                print("Ese paciente no tiene turno.")
    elif opcion == 3:
            if lunes1 == "":
                print("Turno 1 dia lunes: libre.")
            else:
                print("Turno 1 dia lunes:",lunes1)
            if lunes2 == "":
                print("Turno 2 dia lunes: libre.")
            else:
                print("Turno 2 dia lunes:",lunes2)
            if lunes3 == "":
                print("Turno 3 dia lunes: libre.")
            else:
                print("Turno 3 dia lunes:",lunes3)
            if lunes4 == "":
                print("Turno 4 dia lunes: libre.")
            else:
                print("Turno 4 dia lunes:",lunes4)
            if martes1 == "":
                print("Turno 1 dia martes: libre.")
            else:
                print("Turno 1 dia martes:",martes1)
            if martes2 == "":
                print("Turno 2 dia martes: libre.")
            else:
                print("Turno 2 dia martes:",martes2)
            if martes3 == "":
                print("Turno 3 dia martes: libre.")
            else:
                print("Turno 3 dia martes:",martes3)
    elif opcion == 4:
        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1
        
        lunes_libres = 4 - ocupados_lunes

        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1
        
        martes_libres = 3 - ocupados_martes

        if ocupados_lunes > ocupados_martes:
            print("Los dias Lunes tienen mas turnos.")
        elif ocupados_martes > ocupados_lunes:
            print("Los dias Martes tienen mas turnos.")
        else:
            print("Los dias Lunes y Martes tienen la misma cantidad de turnos.")


#Ejercicio 4 — “Escape Room: La Bóveda”

nombre_agente = input("Por favor, ingrese su nombre: ")

while not nombre_agente.replace(" ", "").isalpha():
    print("Error. Ingrese su nombre nuevamente: ")
    nombre_agente = str(input("Ingrese su nombre: "))
print(f"Bienvenido/a agente 🕵️‍♀️🕵️ {nombre_agente}!")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_cerradura = 0 #variable usada para cuando el agente decida cuantas veces quiere forzar la cerradura

#opcion 1: forzar cerradura
#opcion 2: hackear panel
#opcion 3: descansar



while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    print(f"⚡️Energía: {energia}\n⏱️Tiempo: {tiempo}\n🔓Cerraduras abiertas: {cerraduras_abiertas}\n🚨Alarma: {alarma}")
    print("Agente, elija una opción del menú:")
    opcion_menu = input("1. Forzar cerradura. \n2. Hackear panel. \n3. Descansar.\n ")

    while not opcion_menu.isdigit() or int(opcion_menu) < 1 or int(opcion_menu) > 3:
        print("Error. Vuelva a seleccionar un número del menu. ")
        opcion_menu = input("1. Forzar cerradura. \n2. Hackear panel. \n3. Descansar.\n ")
    opcion_menu = int(opcion_menu )

    if opcion_menu == 1:
        forzar_cerradura += 1
        energia -= 20
        tiempo -= 2

        if forzar_cerradura == 3:
            alarma = True
            print("La cerradura se trabó por forzar demasiado 🔒 ")
        else:
            if energia < 40:
                opcion_alarma = input("Hay riesgo de alarma. Elija una opción del 1 al 3: ")

                while not opcion_alarma.isdigit() or int(opcion_alarma) < 1 or int(opcion_alarma) > 3:
                    print("Error. Vuelva a seleccionar un número del 1 al 3. ")
                    opcion_alarma = input("Elija una opción del 1 al 3: ")
                opcion_alarma = int(opcion_alarma)
            
                if opcion_alarma == 3:
                    alarma = True 
                    print("La cerradura se bloqueó 🔐")
            if not alarma:
                cerraduras_abiertas += 1
                print("Se abrió una cerradura. 🔓 Cerraduras abiertas :", cerraduras_abiertas)
    if opcion_menu == 2:
        forzar_cerradura = 0
        energia -= 10
        tiempo -= 3

        for i in range (4):
            codigo_parcial += "A"
            print(f"Hackeando‼️ paso {i+1}/4 - Código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas <3:
            cerraduras_abiertas += 1
            print(f"Cerraduras abiertas! {cerraduras_abiertas} en total 🔓")
    if opcion_menu == 3:
        forzar_cerradura = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        print(f"Ya descansaste, {nombre_agente}. Tienes {energia} energía y {tiempo} tiempo.")        
        if alarma:
            energia -= 10
            print(f"La alarma está activa, perdiste 10 de energía extra.")
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Sistema bloqueado por alarma. ")
        break
if cerraduras_abiertas == 3:
    print(f"FELICITACIONES AGENTE {nombre_agente}, HAS LOGRADO ABRIR LA BÓVEDA.👏🏻")
elif energia <= 0 or tiempo <= 0:
    print(f"Agente {nombre_agente}, HAS SIDO DERROTADO💥")
else:
    print("HAS SIDO BLOQUEADO.")

    
#Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

nombre_gladiador = input("Bienvenido Gladiador, por favor, ingrese su nombre: ")

while not nombre_gladiador.replace(" ", "").isalpha():
    print("Error. Solo se permiten letras. ")
    nombre_gladiador = str(input("Ingrese su nombre: "))
print(f"Bienvenido/a {nombre_gladiador}!")


#Estadisticas
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
dano_base_ataque = 15
dano_base_enemigo = 12
turno_gladiador = True

while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"Gladiador {nombre_gladiador}: tienes {vida_gladiador} de vida. \n Enemigo: tiene {vida_enemigo} de vida. \n Las pociones restantes son: {pociones_vida}")
    print("Seleccione una opción del menú: ")
    menu = input("1. Ataque Pesado\n2.Ráfaga veloz\n3.Curar\n")

    while not menu.isdigit() or int(menu) < 1 or int(menu) > 3:
        print("Error. Vuelva a seleccionar un número del menú. ")
        menu = input("1. Ataque Pesado\n2.Ráfaga veloz\n3.Curar ")
    menu = int(menu)

    if menu == 1:
        if vida_enemigo < 20:
            dano_final = dano_base_ataque * 1.5
            print("Golpe crítico!")
        else:
            dano_final = dano_base_ataque
        vida_enemigo -= dano_final
        print(f"Atacaste al enemigo por {dano_final} puntos de daño!")

    if menu == 2:
        for i in range (3):
            vida_enemigo -= 5                
            print(f"Golpe conectado por 5 de daño")
    if menu == 3:
        if pociones_vida > 0:
            vida_gladiador += 30
            pociones_vida -= 1
        else:
            print("No quedan pociones!")
    if vida_enemigo > 0:
        vida_gladiador -= dano_base_enemigo
        print(f"El enemigo te atacó por {dano_base_enemigo} puntos de daño!")
if vida_gladiador > 0:
    print(f"VICTORIA! {nombre_gladiador} HAS GANADO LA BATALLA!")
else:
    print("DERROTA. Has caído en combate.")






        


            
            

        






        




            







        










            
            






                
    
    
















            








    

















