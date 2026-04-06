# scripts/seed_data.py
# Script para poblar la base de datos con datos de ejemplo para desarrollo y pruebas.

from app.db.session import SessionLocal
from app.modules.users.user_model import User
from app.modules.roles.role_model import Role, Permission
from app.modules.identities.identity_model import Identity
from app.modules.audit.audit_model import AuditLog

from datetime import datetime, UTC
import random
from app.core.security import hash_password

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def seed():
    db = SessionLocal()

    print("🌱 Iniciando seed...")

    # =========================
    # ROLES
    # =========================

    if db.query(Role).count() > 0:
        print("⚠️ Ya existen datos en la tabla de roles, abortando seed")
        return

    admin_role = Role(nombre="admin", descripcion="Rol con todos los permisos")
    profesor_role = Role(nombre="profesor", descripcion="Rol para profesores")
    estudiante_role = Role(nombre="estudiante", descripcion="Rol para estudiantes")

    db.add_all([admin_role, profesor_role, estudiante_role])
    db.commit()

    db.refresh(admin_role)
    db.refresh(profesor_role)
    db.refresh(estudiante_role)

    print("✔ Roles creados")

    # =========================
    # PERMISOS
    # =========================

    permissions_data = [
        "users:read",
        "users:create",
        "users:update",
        "users:delete"
    ]

    permissions = {}

    for name in permissions_data:
        perm = Permission(nombre=name)
        db.add(perm)
        db.flush()
        permissions[name] = perm

    print("✔ Permisos creados")

    # =========================
    # ASIGNAR PERMISOS A ROLES
    # =========================

    # Admin → todos
    admin_role.permissions = list(permissions.values())

    # Profesor → read + update
    profesor_role.permissions = [
        permissions["users:read"],
        permissions["users:update"]
    ]

    # Estudiante → solo read
    estudiante_role.permissions = [
        permissions["users:read"]
    ]

    db.commit()

    print("✔ Permisos asignados a roles")

    # =========================
    # USUARIOS
    # =========================

    users = []

    # ADMINS
    admins = [
        User(nombre="Admin Principal", activo=True),
        User(nombre="Admin Secundario", activo=True),
    ]

    # PROFESORES
    profesores = [
        User(nombre="Profesor García", activo=True),
        User(nombre="Profesor López", activo=True),
        User(nombre="Profesor Martínez", activo=True),
    ]

    # ALUMNOS
    alumnos = [
        User(nombre=f"Alumno {i}", activo=True)
        for i in range(1, 21)
    ]

    users.extend(admins + profesores + alumnos)

    db.add_all(users)
    db.commit()

    print("✔ Usuarios creados")

    # =========================
    # IDENTIDADES
    # =========================

    def create_identity(user, email, role):
        return Identity(
            email=email,
            provider="local",
            password_hash=hash_password("1234"),
            user_id=user.id_usuario,
            rol_id=role.id_rol
        )

    identities = []

    # Admins
    identities.append(create_identity(admins[0], "admin1@robotica.es", admin_role))
    identities.append(create_identity(admins[1], "admin2@robotica.es", admin_role))

    # Profesores
    for i, profesor in enumerate(profesores):
        identities.append(
            create_identity(profesor, f"profesor{i+1}@uah.es", profesor_role)
        )

    # Alumnos (rol por defecto estudiante)
    for i, alumno in enumerate(alumnos):
        identities.append(
            create_identity(alumno, f"alumno{i+1}@uah.es", estudiante_role)
        )

    db.add_all(identities)
    db.commit()

    print("✔ Identidades creadas")

    # =========================
    # AUDIT LOGS
    # =========================

    actions = [
        "LOGIN",
        "LOGOUT",
        "CREATE_USER",
        "DELETE_USER"
    ]

    logs = []

    all_users = admins + profesores + alumnos

    for _ in range(50):
        user = random.choice(all_users)

        log = AuditLog(
            user_id=user.id_usuario,
            action=random.choice(actions),
            resource_type="user",
            resource_id=user.id_usuario,
            description="Acción generada automáticamente",
            ip_address=f"192.168.1.{random.randint(1,255)}",
            user_agent="Mozilla/5.0",
            created_at=datetime.now(UTC)
        )

        logs.append(log)

    db.add_all(logs)
    db.commit()

    print("✔ Logs generados")

    db.close()

    print("🌱 Seed completado correctamente")


if __name__ == "__main__":
    seed()