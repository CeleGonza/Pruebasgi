class celular:
    
    __Marca="Apple"
    __Modelo=""
    __Peso=194
    __Color="negro"
    __Altura=150.9
    _Endendido=False

    def __init__(self,modelo):
        self.modelo=modelo


    def encender_celular(self,encender):
        self.__Encendido=encender

        if self.encender_celular:
            return "El celular se encendió"

        else:
            return "El celular no encendió"


        
    def encender_Linterna(self,encender):
        self.__Linterna=encender


        if self.__Linterna:
            return "Linterna encendida"

        else:
            return "Linterna apagada"


    def estado(self):
        return "El celular"+self.__Modelo+"está "+self.encender_celular()+" y tiene la linterna "+self.__Linterna()
