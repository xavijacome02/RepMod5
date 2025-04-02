import random

class Laptop:
    def __init__(self, marca, procesador, memoria, costo=500, impuesto=10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = int(memoria)
        self.costo = costo
        self.impuesto = impuesto

    def valor_final(self):
        return self.costo + self.impuesto

    def valor_impuesto(self, descuento):
        return (self.costo * descuento) / 100

    # Método estático
    @staticmethod
    def comparar_costo(Laptop1, Laptop2):
        if Laptop1.costo == Laptop2.costo:
            return "Los costos son iguales"
        else:
            return "Los costos son diferentes"

    # Método de clase
    @classmethod
    def asus_laptop(cls, costo):
        marca = 'ASUS'
        procesador = 'i5'
        memoria = 16
        return cls(marca, procesador, memoria, costo)

    # Método de instancia corregido
    def realizar_diagnostico_sistema(self):
        resultado = {
            "Marca": self.marca,
            "Procesador": self.procesador,
            "Memoria RAM": "OK" if self.memoria >= 8 else "Aumentar memoria RAM",
            "Batería": 'OK' if random.choice([True, False]) else 'Cambiar batería',
        }
        return resultado
#metodo estatico
@staticmethod
def comparar_costo(Laptop1,Laptop2):
    if Laptop1.costo==Laptop2.costo:
      return "Los costos son iguales"
    else:
      return "Los costos son diferentes"



#metodo de clase
@classmethod
def asus_laptop(cls,costo):
      marca='ASUS'
      procesador='i5'
      memoria = 16
      return cls(marca,procesador,memoria,costo)




