class prestamos:
    def __init__(self, Rut, Codigo ) -> None:
        self.__Rut=Rut
        self.__Codigo=Codigo
        


    @property
    def Rut(self):
        return self.__Rut
    
    @property
    def Codigo(self):
        return self.__Codigo
    
