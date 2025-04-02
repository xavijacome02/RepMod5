from laptop import Laptop

class Laptop_gaming(Laptop):
  
  def __init__(self, marca, procesador, memoria, tarjeta_graf, costo=500, impuesto=10):
    super().__init__(marca, procesador, memoria, costo, impuesto)
    self.tarjeta_graf=tarjeta_graf
  
  def realizar_diagnostico_sistema(self):
    resultado_diagnostico=super().realizar_diagnostico_sistema()
    resultado_juego = self.realizar_diagnostico_juego()
    resultado_diagnostico["Resultado juegos"]=resultado_juego
    return resultado_diagnostico
  

  def realizar_diagnostico_juego(self):
    juegos = ["FORTNITE",'COD','GTA']
    resultados ={}
    for juego in juegos:
        fps_base = 30
        if "RTX" in self.tarjeta_graf:
          fps =fps_base*3
        elif "GTX" in self.tarjeta_graf:
          fps = fps_base*2
        else:
          fps = fps_base
        resultados [juego] = f"{fps} FPS"
    return resultados
  
  pass