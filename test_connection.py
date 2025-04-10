# test_connection.py
from sqlalchemy import text
from database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("✅ Conexión exitosa a la base de datos.")
except Exception as e:
    print("❌ Error al conectar con la base de datos:")
    print(e)
