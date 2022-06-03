class Doctor:
    def __init__(self):
        self.nombre = "Andres"
        self.apellido = "Guzman"
        self.ciudad = "loja"


doc1 = Doctor()
print("Nombre: " + doc1.nombre)
print("Apellido: " + doc1.apellido)
print("Ciudad: " + doc1.ciudad)

doc1.nombre = "Juan"
doc1.apellido = "Coronel"
doc1.ciudad = "Zamora"
print("--------------------------")
print("Nombre: " + doc1.nombre)
print("Apellido: " + doc1.apellido)
print("Apellido: " + doc1.ciudad)
