import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('personas.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    direccion TEXT,
    telefono TEXT,
    email TEXT,
    fecha_nacimiento DATE
)
''')

# Cargar datos desde el archivo SQL
try:
    with open('personas_desordenadas.sql', 'r', encoding='utf-8') as archivo_sql:
        script_sql = archivo_sql.read()
        cursor.executescript(script_sql)
        conn.commit()
        print(" Datos cargados correctamente.")
except Exception as e:
    print(f" Error al cargar el archivo SQL: {e}")

# Buscar personas cuyo nombre comienza con una letra específica
letra = input(" Ingresa la letra inicial del nombre que deseas buscar: ").strip()
cursor.execute("SELECT * FROM personas WHERE nombre LIKE ?", (letra + '%',))
resultados = cursor.fetchall()

if resultados:
    print(f"\n Resultados para nombres que comienzan con '{letra}':")
    for persona in resultados:
        print(f"ID: {persona[0]}, Nombre: {persona[1]}, Dirección: {persona[2]}, Teléfono: {persona[3]}, Email: {persona[4]}, Fecha de nacimiento: {persona[5]}")
else:
    print(" No se encontraron coincidencias.")


conn.close()