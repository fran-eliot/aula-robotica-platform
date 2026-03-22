from app.db.base import Base
from app.db.session import engine
import app.models 

print("📦 Creando tablas...")
Base.metadata.create_all(bind=engine)
print("✔ Tablas creadas")