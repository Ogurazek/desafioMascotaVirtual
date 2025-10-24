import random

from mascota import imagen


class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.felicidad = 0
        self.hambre = 70
        self.imagen = imagen.inicio
        self.imagen_triste = imagen.triste
        self.imagen_feliz = imagen.feliz
        self.imagen_muerto = imagen.muerto
        self.imagen_disgustado = imagen.disgustado

    def alimentar(self):
        self.felicidad -= random.randint(5, 10)
        if self.felicidad < 0:
            self.felicidad = 0
        if self.hambre == 0:
            print(self.imagen_disgustado)
            print(self.nombre, "esta lleno. Ya no puede comer más!")
        else:
            self.hambre -= random.randint(10, 15)
            if self.hambre < 0:
                self.hambre = 0
            print(self.imagen_feliz)
            print(self.nombre, "ha sido alimentado")

    def jugar(self):
        pass

    def estado_animo(self):
        print("cambiando todo")

    def presentacion(self):
        print(
            f"\n╔════════════════════════════════════╗\n║     Te presento a tu mascota!      ║\n╚════════════════════════════════════╝\n{self.imagen}\tSu nombre es {self.nombre}"
        )

    def despedida(self):
        print(
            f"\n╔════════════════════════════════════╗\n║             Nos vemos!             ║\n╚════════════════════════════════════╝{self.imagen}╔════════════════════════════════════╗\n║        Jueguemos otro día!         ║\n╚════════════════════════════════════╝\n"
        )


interfaz_inicio = "\n╔════════════════════════════════════╗\n║       Bienvenido a tu primer       ║\n║          mascota virtual!          ║\n╚════════════════════════════════════╝\n"
interfaz_juego = "\n╔════════════════════════════════════╗\n║       Opciones disponibles:        ║\n║                                    ║\n║ 1 - Alimentar            ║\n║ 4 - Salir                          ║\n║                                    ║\n╚════════════════════════════════════╝\n"


print(interfaz_inicio)

nombre = input("Elige un nombre para tu mascota: ")
mascota = MascotaVirtual(nombre)
mascota.presentacion()

while True:
    print(interfaz_juego)
    opcion = int(input("Elija una opción: "))
    if opcion == 1:
        mascota.alimentar()
    elif opcion == 4:
        mascota.despedida()
        break


# Traten de hacerlo con el match, así práctican esa forma de hacerlo...


# match opcion:
# case "1":
# mascota.alimentar()
# case "4":
# mascota.despedida()
# break
# case _:
# default
