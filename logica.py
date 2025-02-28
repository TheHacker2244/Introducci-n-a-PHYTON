#un cajero automatico
usuario = list()

usuario.append("TheHacker2244")
usuario.append("1234")
usuario.append(1000)

recibo = list()
recibo.append(["123",600])
recibo.append(["124",845])
recibo.append(["125",67])
recibo.append(["126",500])
recibo.append(["127",100])

acciones = list()
acciones.append("Depositar")
acciones.append("Depositar")
acciones.append("Depositar")
acciones.append("Depositar")

usuario2 = list()
usuario2.append("")
usuario2.append("")
usuario2.append("")

def registrar():
    usuarioRegistrado = list()
    usuarioC = ("Ingrese su nombre: ")
    usuarioRegistrado.append("Ingrese su password")

    if usuarioC == usuario[0]:
        if usuarioRegistrado[1] == usuario[1]:
            print("Bienvenido")