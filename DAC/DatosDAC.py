import pyodbc


class DatosDAC:

    def conectar(self):
        conexion = pyodbc.connect(
            "DRIVER={ODBC Driver 18 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=PruebaEquipo;"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )
        return conexion

    def guardar(self, dato):
        conexion = self.conectar()

        cursor = conexion.cursor()

        cursor.execute(
            "INSERT INTO Datos (Valor) VALUES (?)",
            dato.valor
        )

        conexion.commit()
        conexion.close()

    def obtener_ultimo(self):
        conexion = self.conectar()

        cursor = conexion.cursor()

        cursor.execute(
            "SELECT TOP 1 Valor FROM Datos ORDER BY Id DESC"
        )

        resultado = cursor.fetchone()

        conexion.close()

        if resultado:
            return resultado[0]

        return None