from Persona import persona
from conexion import Conexion
from beautifultable import beautifultable

class personaDAO:
    def __init__(self) -> None:
        pass
    def eliminarPersona(self, rut):
        if self.buscarPersona(rut) != None:
            Conexion.cursor.execute("delete from PERSONA whare rut=:1", [rut])
            Conexion.connection.commit()
            return "Se ha elimido correctamente"
        else:
            return "No se ha podido crear"

    def buscarPersona(self, rut)->persona:
        Conexion.cursor.execute("select * from PERSONA where rut=:1", [rut])
        row=Conexion.cursor.fetchone()
        if row is None:
            return  None
        else:
            return persona (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    
    def insertarPersona(self, Persona):
        if self.isertarPerosna(Persona) != None:
            Conexion.cursor.excute("""
            insert into deuda value(:1,:2,:3,:4,:5,:6,:7) 
            """,[Persona.Rut, Persona.Nombre, Persona.Apellido, Persona.Ciudad, Persona.Direccion, Persona.Telefono, Persona.ID_tipoPersona])
            Conexion.connection.commit()
            return "Los datos fueron ingresados de forma correcta"
        else:
            return "persona ya existe"
        
    def obtenerPersona(self)->None:
        tabla=beautifultable()
        tabla.columns.header=["Rut", "Nombre", "Apellido", "Ciudad", "Direccion", "Telefono", "ID_tipoPersona"]
        for row in Conexion.cursor.execute("Select*from persona order by 1"):
            tabla.rows.appedn(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print("persona no ingresado")