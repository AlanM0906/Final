import psycopg2
import sys
import pprint
import getpass

boletos = 0
total = 0
sub_total = 0
primeraClase = 0
segundaClase = 0
terceraClase = 0
descuentoPrimera = 0
comidaPrimera = 0
aguaPrimera = 0
peliPrimera = 0
comidaSegunda = 0
aguaSegunda = 0
peliSegunda = 0
comidaTercera = 0
aguaTercera = 0
peliTercera = 0
descuento = 0

PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "Abuelokiko50"
PSQL_DB = "final"

connection_address = """
    host=%s port=%s user=%s password=%s dbname=%s
""" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
connection = psycopg2.connect(connection_address)
cursor = connection.cursor()

def admin():
    
    usuario_admin = input("Usuario: ")
    pas_admin = getpass.getpass(prompt = 'Constraseña: ',stream = None)
    SQL = "select * from superu where usuario=%s and contrasenia = %s;"
    cursor.execute(SQL,(usuario_admin,pas_admin))
    registros = cursor.fetchall()
    if (registros):
        print("¿Qué desea realizar?")
        print("1. Agregar Operador")
        print("2. Eliminar Operador")
        print("3. Agregar Administrador")
        print("4. Eliminar Administrador")
        print("5. Regresar al menu principal")
        op = int(input(": "))
        while(op <5):
            if(op == 1):
                print()
                print("AGREGARA UN NUEVO OPERADOR")
                nom_op = input("Ingrese el usuario nuevo: ")
                pass_op= input("Ingrese la contraseña nueva: ")
                SQL = "select * from operadores where usuario= ('%s');" % (nom_op)
                cursor.execute(SQL)
                registros2 = cursor.fetchall()
                if(registros2):
                    print("Ese usuario ya existe, intente con otro.")
                else:
                    
                    print()
                    SQL2 = "insert into operadores (usuario,contrasenia) values (%s,%s);"
                    cursor.execute(SQL2, (nom_op,pass_op))
                    connection.commit()
                    print("El operador fue agregado con exito.")
            elif(op == 2):
                print()
                print("ELIMINAR UN OPERADOR")
                nom_op = input("Ingrese el usuario del operador: ")
                SQL2 = "delete from operadores where usuario = ('%s');" % (nom_op)
                cursor.execute(SQL2)
                connection.commit()
                print("Se elimino el operador con exito.")
            elif(op == 3):
                print()
                print("AGREGARA UN NUEVO ADMINISTRADOR")
                nom_op = input("Ingrese el usuario nuevo: ")
                pass_op= input("Ingrese la contraseña nueva: ")
                SQL = "select * from superu where usuario= ('%s');" % (nom_op)
                cursor.execute(SQL)
                registros2 = cursor.fetchall()
                if(registros2):
                    print("Ese usuario ya existe, intente con otro.")
                else:
                    print()
                    SQL2 = "insert into superu (usuario,contrasenia) values (%s,%s);"
                    cursor.execute(SQL2, (nom_op,pass_op))
                    connection.commit()
                    print("El administrador fue agregado con exito.")
            elif(op == 4):
                print()
                print("ELIMINAR UN ADMINISTRADOR")
                nom_op = input("Ingrese el usuario del administrador: ")
                SQL2 = "delete from superu where usuario = ('%s');" % (nom_op)
                cursor.execute(SQL2)
                connection.commit()
            print()
            print("¿Desea realizar otra función?")
            print("1. Agregar Operador")
            print("2. Eliminar Operador")
            print("3. Agregar Administrador")
            print("4. Eliminar Administrador")
            print("5. Regresar al menu principal")
            op = int(input(": "))
    else:
        print("Usuario y/o contraseña invalidos")

def operador():
    usuario_op = input("Usuario: ")
    pas_op = getpass.getpass(prompt = 'Constraseña: ',stream = None)
    SQL = "select * from operadores where usuario=%s and contrasenia = %s;"
    cursor.execute(SQL,(usuario_op,pas_op))
    registros = cursor.fetchall()
    if (registros):
        def agregar_boletos():
            global sub_total
            global boletos
            global primeraClase
            global segundaClase
            global terceraClase
            global descuentoPrimera
            global comidaPrimera 
            global aguaPrimera 
            global peliPrimera 
            global comidaSegunda 
            global aguaSegunda 
            global peliSegunda 
            global comidaTercera 
            global aguaTercera 
            global peliTercera 
            boletos = boletos + 1
            print("¿De que tipo sera su boleto?")
            print("1. Primera Clase. Comida: Q50 Agua: Q35 Pelicula Q70")
            print("2. Segunda Clase. Comida: Q40 Agua: Q25 Pelicula Q55")
            print("2. Tercera Clase. Comida: Q25 Agua: Q10 Pelicula Q25")
            tipo = int(input(": "))
            if (tipo == 1):
                primeraClase = primeraClase + 1
                precioComida = 50
                precioAgua = 35
                precioPeli = 70
            elif (tipo == 2):
                segundaClase = segundaClase +1
                precioComida = 40
                precioAgua = 25
                precioPeli = 55
            elif (tipo == 3):
                terceraClase = terceraClase +1
                precioComida = 25
                precioAgua = 10
                precioPeli = 25

            print("¿Desea agregar comida?")
            print("1. Si")
            print("2. No")
            op1 = int(input(""))
            if (op1 == 1):
                sub_total = sub_total + precioComida
                if(tipo == 1):
                    comidaPrimera = comidaPrimera + 1
                elif(tipo == 2):
                    comidaSegunda = comidaSegunda + 1
                elif(tipo == 3):
                    comidaTercera = comidaTercera +1
            print("¿Desea agregar Agua?")
            print("1. Si")
            print("2. No")
            op2 = int(input(""))
            if (op2 == 1):
                sub_total = sub_total + precioAgua
                if(tipo == 1):
                    aguaPrimera = aguaPrimera + 1
                elif(tipo == 2):
                    aguaSegunda = aguaSegunda + 1
                elif(tipo == 3):
                    aguaTercera = aguaTercera +1
            print("¿Desea agregar una pelicula?")
            print("1. Si")
            print("2. No")
            op3 = int(input(""))
            if (op3 == 1):
                sub_total = sub_total + precioPeli
                if(tipo == 1):
                    peliPrimera = peliPrimera + 1
                elif(tipo == 2):
                    peliSegunda = peliSegunda + 1
                elif(tipo == 3):
                    peliTercera = peliTercera +1

            if(tipo == 1 and op1 == 1 and op2 == 1 and op3 == 1):
                descuentoPrimera = descuentoPrimera + 7.75

        def limpiar():
            global boletos 
            global total
            global sub_total
            global primeraClase 
            global segundaClase
            global terceraClase

            boletos = 0
            total = 0
            sub_total = 0
            primeraClase = 0
            segundaClase = 0
            terceraClase = 0

            print("Se eliminaron los boletos")
            SQL = "delete from boletos;"
            cursor.execute(SQL)
            connection.commit()
        def calcular():
            global boletos 
            global total
            global sub_total
            global primeraClase 
            global segundaClase
            global terceraClase
            global descuentoPrimera
            global comidaPrimera 
            global aguaPrimera 
            global peliPrimera 
            global comidaSegunda 
            global aguaSegunda 
            global peliSegunda 
            global comidaTercera 
            global aguaTercera 
            global peliTercera
            global descuento
            if(boletos <10):
                descuento = descuentoPrimera
                total = sub_total - descuento
            else:
                descuento = (sub_total - descuentoPrimera)/10
                total = sub_total - descuento
            print("Se tienen ",boletos,"boleto/s. De los cuales ",primeraClase," son de primera clase, ",segundaClase," son de segunda clase y ",terceraClase," son de tercera clase.")
            print("De primera clase se solicitaron : ",comidaPrimera," comida/s, ",aguaPrimera," agua/s y ",peliPrimera,"pelicula/s")
            print("De segunda clase se solicitaron : ",comidaSegunda," comida/s, ",aguaSegunda," agua/s y ",peliSegunda,"pelicula/s")
            print("De tercera clase se solicitaron : ",comidaTercera," comida/s, ",aguaTercera," agua/s y ",peliTercera,"pelicula/s")
            print("El total a pagar es: Q",total)
            
        def reporte():
            global total
            global sub_total
            global boletos
            global primeraClase
            global segundaClase
            global terceraClase
            global descuentoPrimera
            global comidaPrimera 
            global aguaPrimera 
            global peliPrimera 
            global comidaSegunda 
            global aguaSegunda 
            global peliSegunda 
            global comidaTercera 
            global aguaTercera 
            global peliTercera
            global descuento
            bol = str(boletos)
            prim= str(primeraClase)
            seg = str(segundaClase)
            ter = str(terceraClase)
            sub = str(sub_total)
            off = str(descuento)
            total=str(total)
            if(boletos >0):
                nombre = input("¿A nombre de quien se registran los boletos?")
                SQL = "insert into boletos (boletos, primera, segunda, tercera,sub,off,total,nombre,operador) values (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                cursor.execute(SQL, (bol, prim, seg, ter, sub, off, total,nombre,usuario_op))
                connection.commit()
            print("Cantidad de boletos, Primera Clase, Segunda Clase, Tercera Clase, Subtotal, Descuento, Total,Nombre,Operador")
            SQL2 = "select * from boletos;"
            cursor.execute(SQL2)
            registros = cursor.fetchall()
            pprint.pprint(registros)
            comidaPrimera = 0
            comidaSegunda = 0
            comidaTercera = 0
            aguaPrimera = 0
            aguaSegunda = 0
            aguaTercera = 0
            peliPrimera = 0
            peliSegunda = 0
            peliTercera = 0
            boletos = 0
            primeraClase = 0
            segundaClase = 0
            terceraClase = 0
            
            

        print("*****AEROLINAS SAN CARLOS*****")
        print("1. Agregar boleto")
        print("2. Limpiar")
        print("3. Calcular")
        print("4. Factura")
        print("5. Salir")
        print("")
        opciones = int(input("Escoja una opcion del menu: "))
        while (opciones < 1 or opciones >5):
            print("Esa opción no esta en el menu desplegado")
            opciones = int(input("Escoja una opcion del menu: "))
        while(opciones<=4):
            programas = [agregar_boletos,limpiar,calcular,reporte]
            programas[opciones-1]()
            print("")
            print("1. Agregar otro boleto")
            print("2. Limpiar")
            print("3. Calcular")
            print("4. Factura")
            print("5. Salir al Menú Principal")
            opciones = int(input("Escoja una opcion del menu: "))
        
    else:
        print("Usuario y/o contraseña invalidos")

def salir():
    print("Gracias por volar con nosotros, que tengas un buen viaje. ")
    cursor.close()
    connection.close()
    sys.exit()

try:
    print()
    print("*******MENÚ PRINCIAPL*******")
    print()
    print("1. Iniciar Sesion Como Administrador")
    print("2. Iniciar Sesion Como Opeador")
    print("3. Cerrar la aplicacion")
    print("")
    op_menu = int(input("¿Qué desea hacer? "))
    print("")
    while(op_menu <1 or op_menu >3):
        print("Esa opcion no se encuentra entre las opciones posibles")
        op_menu = int(input("¿Qué desea hacer? "))
    while(op_menu <= 3):
        try:
            programas = [admin,operador,salir]
            programas[op_menu-1]()
            print()
            print("*******MENÚ PRINCIAPL*******")
            print()
            print("1. Iniciar Sesion Como Administrador")
            print("2. Iniciar Sesion Como Opeador")
            print("3. Cerrar la aplicacion")
            print("")
            op_menu = int(input("¿Qué desea hacer? "))
            print()
        except(ValueError):
            print("Ocurrio un problema durante la ejecucion del programa.")
            print("")
            op_menu = int(input("¿Qué desea hacer? "))
except(ValueError):
    print("A ocurrido un error, vuelva a intentarlo.")
        
