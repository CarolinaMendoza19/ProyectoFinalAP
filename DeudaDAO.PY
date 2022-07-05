from Deuda import deuda
from conexion import Conexion
from beautifultable import beautifultable

class deudaDAO:
    def __init__(self) -> None:
        pass
    
    def eliminarDeuda(self, ID_deuda):
        if self.buscarDeuda(ID_deuda) != None:
            Conexion.cursor.execute("delete from DEUDA whare ID_dedua=:1", [ID_deuda])
            Conexion.connection.commit()
            return "Se ha elimido correctamente"
        else:
            return "No se ha podido crear"

    def buscarDedua(self, ID_deuda)->deuda:
        Conexion.cursor.execute("select * from DEDUA where ID_deuda =:1", [ID_deuda])
        row=Conexion.cursor.fetchone()
        if row is None:
            return  None
        else:
            return deuda (row[0], row[1], row[2], row[3], row[4])
    
    def insertarDeuda(self, Deuda):
        if self.insertarDeuda(Deuda) != None:
            Conexion.cursor.excute("""
            insert into deuda value(:1,:2,:3,:4,:5) 
            """,[Deuda.ID_dedua, Deuda.Titulo_libro, Deuda.Dias_retraso, Deuda.Monto_deuda, Deuda.ID_prestamo])
            Conexion.connection.commit()
            return "Los datos fueron ingresados de forma correcta"
        else:
            return "deuda ya existe"
        
    def obtenerDeuda(self)->None:
        tabla=beautifultable()
        tabla.columns.header=["ID_Deuda", "Titulo_libro", "Dias_retraso", "Monto_deuda", "ID_prestamo"]
        for row in Conexion.cursor.execute("Select*from deuda order by 1"):
            tabla.rows.appedn(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print("deuda no ingresado")