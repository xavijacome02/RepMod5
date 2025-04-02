from laptop import Laptop
from laptop_gaming import Laptop_gaming
from Laptop_Business import Laptop_Business


Laptop_pepito = Laptop("Lenovo","i7","32")
Laptop_Maria = Laptop("Lenovo","i7","32",600)



laptop_juanito = Laptop_gaming('ASUS','i7','64','RTX 8GB')
print(laptop_juanito.realizar_diagnostico_sistema())


laptop_empresarial = Laptop_Business("Dell", "i7", 16, 512, 8)
print(laptop_empresarial.realizar_diagnostico_sistema())


#for numero in range (1,1001):
#    asus_laptop = Laptop.asus_laptop(numero)
#    print(asus_laptop.__dict__)
#
#print(Laptop_pepito.__dict__)
#print(Laptop_pepito.valor_final())
#print(f"El valor de descueno : {Laptop_pepito.valor_impuesto(10)}")
#print(laptop_juanito.__dict__)

