from conexion import Conexion


class BaseDato():
    def __init__(self) -> None:
        pass

    def validarExistenciaTabla(self) -> bool:
        Conexion.cursor.execute('''
        select * from user_tables where table_name = UPPER('PERSONA')
        UNION
        select * from user_tables where table_name = UPPER('PRESTAMOS')
        UNION
        select * from user_tables where table_name = UPPER('LIBRO')
        UNION
        select * from user_tables where table_name = UPPER('TIPO_PERSONA')
        UNION
        select * from user_tables where table_name = UPPER('DEUDA')
        ''')
        rows = Conexion.cursor.fetchall()
        if len(rows) > 0:
            return True
        else:
            return False

    def eliminarTablas(self) -> str:
        if self.validarExistenciaTabla() == True:
            Conexion.cursor.execute('''
            drop table PERSONA
            ''')
            Conexion.cursor.execute('''
            drop table PRESTAMOS
            ''')
            Conexion.cursor.execute('''
            drop table LIBRO
            ''')
            Conexion.cursor.execute('''
            drop table TIPO_PERSONA
            ''')
            Conexion.cursor.execute('''
            drop table DEUDA
            ''')
            Conexion.connection.commit()
            return '''SE ELIMINARON LAS SIGUENTES TABLAS
            -Persona
            -Prestamos
            -Libro
            -Tipo_Persona
            -Deuda'''
        else:
            return 'Las tablas no existen'

    def crearTablas(self):
        if self.validarExistenciaTabla() == False:
            Conexion.cursor.execute('''
            CREATE TABLE PERSONA (
                id_rut NUMBER(12),
                nombre VARCHAR2(20),
                apellido VARCHAR2(20),
                ciudad VARCHAR2(20),
                direccion VARCHAR2(20),
                telefono NUMBER(12),
                CONSTRAINT PK_ID_Persona PRIMARY KEY(id_rut)
                );
            ''')
            Conexion.cursor.execute('''
            CREATE TABLE PRESTAMOS(
                ID_RUT NUMBER (12),
                ID_CODIGO NUMBER(12),
                CONSTRAINT FK_ID_PRESTAMOS PRIMARY KEY(id_rut)
                );

            ''')
            Conexion.cursor.execute('''
            CREATE TABLE libro(
                id_codigo NUMBER(10),
                titulo VARCHAR2(40),
                autor VARCHAR2(25),
                fecha_entrega VARCHAR2(11),
                fecha_prestamo VARCHAR2(11),
                CONSTRAINT PK_ID_libro PRIMARY KEY(id_codigo)
                );

            ''')
            Conexion.cursor.execute('''
            CREATE TABLE tipo_persona(
                id_persona NUMBER (10),
                nombre VARCHAR2(30),
                CONSTRAINT PK_ID_TipoPersona PRIMARY KEY(id_persona)
                );

            ''')
            Conexion.cursor.execute('''
            CREATE TABLE deuda (
                id_deuda NUMBER(10),
                titulo_libro VARCHAR2(40),
                dias_retraso VARCHAR2(30),
                monto_deuda VARCHAR2(20),
                CONSTRAINT PK_ID_DEUDA PRIMARY KEY(id_deuda)
                );

            ''')