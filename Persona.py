class persona:
    def __init__(self, Rut, Nombre, Apellido, Ciudad, Direccion,Telefono, ID_TipoPersona ) -> None:
        self.__Rut=Rut
        self.__Nombre=Nombre
        self.__Apellido=Apellido
        self.__Ciudad=Ciudad
        self.__Direccion=Direccion
        self.__Telefono=Telefono
        self.__ID_TipoPersona=ID_TipoPersona


    @property
    def Rut(self):
        return self.__Rut
    
    @property
    def Nombre(self):
        return self.__Nombre
    
    @property
    def Apellido(self):
        return self.__Apellido
    
    @property
    def Ciudad(self):
        return self.__Ciudad
    
    @property
    def Direccion(self):
        return self.__Direccion

    @property
    def Telefono(self):
        return self.__Telefono
    @property
    def ID_TipoPersona(self):
        return self.__ID_TipoPersona
    
    
    

    
