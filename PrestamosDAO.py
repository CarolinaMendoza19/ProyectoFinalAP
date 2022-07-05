from Prestamos import prestamos
from conexion import Conexion
from beautifultable import beautifultable

class prestamosDAO:
    def __init__(self) -> None:
        pass
    def eliminarPrestamos(self, rut):
        if self.buscarPrestamos(rut) != None:
            Conexion.cursor.execute("delete from PRESTAMOS whare rut=:1", [rut])
            Conexion.connection.commit()
            return "Se ha elimido correctamente"
        else:
            return "No se ha podido crear"

    def buscarPrestamos(self, rut)->prestamos:
        Conexion.cursor.execute("select * from PRESTAMOS where rut =:1", [rut])
        row=Conexion.cursor.fetchone()
        if row is None:
            return  None
        else:
            return prestamos (row[0], row[1])
    
    def insertarPrestamos(self, Prestamos):
        if self.isertarPrestamos(Prestamos) != None:
            Conexion.cursor.excute("""
            insert into prestamos value(:1,:2) 
            """,[Prestamos.Rut, Prestamos.Codigo])
            Conexion.connection.commit()
            return "Los datos fueron ingresados de forma correcta"
        else:
            return "tipo persona ya existe"
        
    def obtenerPrestamos(self)->None:
        tabla=beautifultable()
        tabla.columns.header=["Rut", "Codigo"]
        for row in Conexion.cursor.execute("Select*from PRESTAMOS order by 1"):
            tabla.rows.appedn(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print("Prestamos no ingresado")