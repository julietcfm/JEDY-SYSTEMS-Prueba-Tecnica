from DAC.DatosDAC import DatosDAC
from DTO.DatoDTO import DatoDTO


class DatosBL:

    def guardar_dato(self, valor):
        dato = DatoDTO(valor)
        dac = DatosDAC()
        dac.guardar(dato)

    def obtener_dato(self):
        dac = DatosDAC()
        return dac.obtener_ultimo()