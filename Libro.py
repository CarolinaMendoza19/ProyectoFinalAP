class libro:
    def __init__(self, Codigo, Titulo, Autor, Fecha_entrega, Fecha_prestamo ) -> None:
        self.__Codigo=Codigo
        self.__Titulo=Titulo
        self.__Autor=Autor
        self.__Fecha_entrega=Fecha_entrega
        self.__Fecha_prestamo=Fecha_prestamo

    @property
    def Codigo(self):
        return self.__Codigo

    @property
    def Titulo(self):
        return self.__Titulo
    
    @property
    def Autor(self):
        return self.__Autor
    
    @property
    def Fecha_entrega(self):
        return self.__Fecha_entrega
    
    @property
    def Fecha_prestamo(self):
        return self.__Fecha_prestamo
    

    

    