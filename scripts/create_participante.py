from app.db.session import SessionLocal
from app.modules.users.user_model import User
from app.modules.users.identity_model import Identity
from app.modules.users.role_model import Role
from app.core.security import hash_password

db = SessionLocal()

# Buscar rol participante
rol_participante = db.query(Role).filter(
    Role.nombre == "participante"
).first()

if not rol_participante:
    print("No existe rol participante")
    exit()

# Crear usuario
nuevo_usuario = User(
    nombre="Carlos Participante",
    activo=True
)

db.add(nuevo_usuario)
db.commit()
db.refresh(nuevo_usuario)

# Crear identidad local
identidad = Identity(
    email="carlos_participante@eurobot.es",
    provider="local",
    password_hash=hash_password("123456"),
    user_id=nuevo_usuario.id_usuario,
    rol_id=rol_participante.id_rol
)

db.add(identidad)
db.commit()

print("Usuario participante creado correctamente")