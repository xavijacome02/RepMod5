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

#metodo clase   
    @classmethod
    def auto_ano(cls):
        marca='Toyota'
        modelo='xxxxx'
        ano=2025
        return cls(marca,modelo,ano)
#metodo estatico
    @staticmethod
    def validar_auto(auto1,auto2):
        if auto1.kilometraje==auto2.kilometraje:
            return "Tienen el mismo kilometraje"
        else:
            return"Tienen distinto los kilometrajes"
    
        


# Prueba
Prueba_auto = Auto("Chevrolet", "Joy", 2022)
Prueba_auto2=Auto("Toyota", "M5", 2023,1000)

auto_ano = Prueba_auto.auto_ano()
print(f"Prueba del metodo clase --> {auto_ano.__dict__}")
print(f"Prueba del metodo estatico ---> {Auto.validar_auto(Prueba_auto,Prueba_auto2)}")


print(Prueba_auto.__dict__)
print(Prueba_auto.mostrar_informacion())
print(Prueba_auto.actualizar_kilometraje(50))
print(Prueba_auto.realizar_viaje(100))
print(Prueba_auto.estado_auto())
