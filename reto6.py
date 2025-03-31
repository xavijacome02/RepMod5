class Auto:
    def __init__(self, marca, modelo, ano, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.ano}"

    def actualizar_kilometraje(self, kilometraje):
        if kilometraje >= self.kilometraje:
            self.kilometraje = kilometraje
            return f"Kilometraje actualizado a {self.kilometraje} km."
        else:
            return "No se puede reducir el kilometraje."

    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
            return f"Se han añadido {kilometros} km al kilometraje."
        else:
            return "La cantidad de kilómetros debe ser positiva."

    def estado_auto(self):
        if self.kilometraje < 20000:
            return "Estoy como nuevo."
        elif 20000 <= self.kilometraje <= 100000:
            return "Ya estoy usado."
        else:
            return "¡Ya déjame descansar por favor!"

# Prueba
Prueba_auto = Auto("Chevrolet", "Joy", 2022)

print(Prueba_auto.__dict__)
print(Prueba_auto.mostrar_informacion())
print(Prueba_auto.actualizar_kilometraje(50))
print(Prueba_auto.realizar_viaje(100))
print(Prueba_auto.estado_auto())
