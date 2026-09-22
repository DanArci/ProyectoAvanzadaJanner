from sqlmodel import create_engine

# Crear la conexion con la base de datos en supabase
DATABASE_URL = ("postgresql://postgres.usorytamkdtoegtzgsdt:Zn0jjGoR3gtXm5zv@aws-0-ca-central-1.pooler.supabase.com:5432/postgres")
engine = create_engine(DATABASE_URL)
