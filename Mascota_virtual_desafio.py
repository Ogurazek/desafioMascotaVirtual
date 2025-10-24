import random

from mascota import imagen


class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.felicidad = 0
        self.hambre = 0
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
        pass

    def presentacion(self):
        print(
            f"\n╔════════════════════════════════════╗\n║     Te presento a tu mascota!      ║\n╚════════════════════════════════════╝\n{self.imagen}\tSu nombre es {self.nombre}"
        )

    def despedida(self):
        print(
            f"\n╔════════════════════════════════════╗\n║             Nos vemos!             ║\n╚════════════════════════════════════╝{self.imagen}╔════════════════════════════════════╗\n║        Jueguemos otro día!         ║\n╚════════════════════════════════════╝\n"
        )


# Crear una instancia de MascotaVirtual

# Si te animas crea una interfaz para poder interactuar con tu mascota
