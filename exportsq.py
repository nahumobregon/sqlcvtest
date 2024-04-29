import pyodbc

# Establecer la cadena de conexión
server = 'DESKTOP-T1J8AKE\\ISITA'
database = 'Recursividad'
username = 'sa'
password = 'Nhm27noc$.'
conn_str = 'DRIVER=ODBC Driver 17 for SQL Server;SERVER=' + \
    server+';DATABASE='+database+';UID='+username+';PWD='+password

print(conn_str)

# Conectarse a la base de datos
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Consulta para obtener el texto del procedimiento almacenado
stored_proc_name = 'testing01'
query = ("SELECT OBJECT_DEFINITION(OBJECT_ID('" +
         stored_proc_name+"')) AS ProcedureText")

print(query)

cursor.execute(query)
row = cursor.fetchone()

if row:
    procedure_text = row[0]

    # Guardar el texto del procedimiento en un archivo
    file_name = f'{stored_proc_name}.sql'
    with open(file_name, 'w') as file:
        file.write(procedure_text)
        print('Procedimiento almacenado exportado exitosamente a ',
              {file_name})

# Cerrar la conexión
conn.close()
