from Libro import libro
from conexion import Conexion
from beautifultable import beautifultable

class libroDAO:
    def __init__(self) -> None:
        pass
    def eliminarLibro(self, codigo):
        if self.buscarLibro(codigo) != None:
            Conexion.cursor.execute("delete from LIBRO whare codigo=:1", [codigo])
            Conexion.connection.commit()
            return "Se ha elimido correctamente"
        else:
            return "No se ha podido crear"

    def buscarLibro(self, codigo)->libro:
        Conexion.cursor.execute("select * from LIBRO where codigo=:1", [codigo])
        row=Conexion.cursor.fetchone()
        if row is None:
            return  None
        else:
            return libro (row[0], row[1], row[2], row[3], row[4])
    
    def insertarLibro(self, Libro):
        if self.isertarLibro(Libro) != None:
            Conexion.cursor.excute("""
            insert into deuda value(:1,:2,:3,:4,:5) 
            """,[Libro.Codigo, Libro.Titulo, Libro.Autor, Libro.Fehca_entrega, Libro.Fecha_entrega])
            Conexion.connection.commit()
            return "Los datos fueron ingresados de forma correcta"
        else:
            return "libro ya existe"
        
    def obtenerLibro(self)->None:
        tabla=beautifultable()
        tabla.columns.header=["Codigo", "Titulo", "Autor", "Fecha_entrega", "Fecha_entrega"]
        for row in Conexion.cursor.execute("Select*from libro order by 1"):
            tabla.rows.appedn(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print("libro no ingresado")