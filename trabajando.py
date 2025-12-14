
   
def crear_archivo(nombre, matricula, correo, telefono):
    with open(nombre + ".txt", "w") as archivo:
        archivo.write(f"Matricula: {matricula}\n")
        archivo.write(f"Correo: {correo}\n")
        archivo.write(f"Telefono: {telefono}\n")
    print(f"Archivo {nombre}.txt creado exitosamente.")

def leer_archivo(nombre):
    try:
        with open(nombre + ".txt", "r") as archivo:
            contenido = archivo.read()
            print(f"\nContenido del archivo {nombre}.txt:\n")
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo {nombre}.txt no existe.")

nombre_usuario = input("Ingrese el nombre del archivo a crear: ")
matricula = input("Ingrese la matrícula: ")
correo = input("Ingrese el correo: ")
telefono = input("Ingrese el teléfono: ")

crear_archivo(nombre_usuario, matricula, correo, telefono)
leer_archivo(nombre_usuario)

print("Archivo creado y leído exitosamente.")