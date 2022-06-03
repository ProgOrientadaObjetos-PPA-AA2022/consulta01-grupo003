class Persona:
    def __init__(self, edad, nombre, ocupacion):
        self.edad = edad
        self.nombre = nombre
        self.ocupacion = ocupacion

        # Creación de un nuevo método
    def presentar(self):
        presentacion = "Hola soy {}, mi edad es {} y mi ocupación es {}"
        print(presentacion.format(self.nombre, self.edad, self.ocupacion))


Persona1 = Persona(27, "Juan", "Abogado")
# Llamamos al método
Persona1.presentar()
