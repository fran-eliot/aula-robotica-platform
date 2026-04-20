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
        print("⚠️ Base ya inicializada. Ejecuta reset antes del seed.")
        return

    admin_role = Role(nombre="admin", descripcion="Rol con todos los permisos")
    profesor_role = Role(nombre="profesor", descripcion="Rol para profesores")
    estudiante_role = Role(nombre="estudiante", descripcion="Rol para estudiantes")
    user_uah_role = Role(nombre="uah_user", descripcion="Acceso inicial mediante SSO UAH (SAML)")

    db.add_all([admin_role, profesor_role, estudiante_role, user_uah_role])
    db.commit()

    db.refresh(admin_role)
    db.refresh(profesor_role)
    db.refresh(estudiante_role)
    db.refresh(user_uah_role)

    print("✔ Roles creados")

    # =========================
    # PERMISOS
    # =========================

    permissions_data = [
        "users:read",
        "users:create",
        "users:update",
        "users:delete",

        "roles:read",
        "roles:create",
        "roles:update",
        "roles:delete",

        "identities:read",
        "identities:create",
        "identities:update",
        "identities:delete",

        "dashboard:read",
        "students:read",
        "audit:read"
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
        permissions["users:update"],
        permissions["dashboard:read"],
        permissions["students:read"]
    ]

    # Estudiante → solo read
    estudiante_role.permissions = [
        permissions["dashboard:read"],
        permissions["students:read"]
    ]

    # Estudiante UAH → solo read
    user_uah_role.permissions = [
        permissions["dashboard:read"],
        permissions["students:read"]
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

    # Estudiantes UAH (SAML) (sOLO 1 PARA DEMO)
    uah_users = [
        User(nombre=f"User UAH", activo=True)
    ]

    users.extend(admins + profesores + alumnos + uah_users)

    db.add_all(users)
    db.commit()

    print("✔ Usuarios creados")

    # =========================
    # ASIGNAR ROLES A USUARIOS (RBAC REAL)
    # =========================

    # Admins
    for user in admins:
        user.roles.append(admin_role)

    # Profesores
    for user in profesores:
        user.roles.append(profesor_role)

    # Estudiantes
    for user in alumnos:
        user.roles.append(estudiante_role)

    # Estudiante UAH (SAML)
    for user in uah_users:
        user.roles.append(user_uah_role)

    db.commit()

    # =========================
    # IDENTIDADES
    # =========================

    def create_identity(user, email):
        return Identity(
            email=email,
            provider="local",
            password_hash=hash_password("1234"),
            user_id=user.id_usuario
        )
    
    def create_saml_identity(user, email):
        return Identity(
            email=email,
            provider="uah_saml",
            password_hash=None,  # No se almacena contraseña para SAML
            user_id=user.id_usuario
        )

    identities = []

    # Admins
    identities.append(create_identity(admins[0], "admin1@robotica.es"))
    identities.append(create_identity(admins[1], "admin2@robotica.es"))

    # Profesores
    for i, profesor in enumerate(profesores):
        identities.append(
            create_identity(profesor, f"profesor{i+1}@uah.es")
        )

    # Alumnos (rol por defecto estudiante)
    for i, alumno in enumerate(alumnos):
        identities.append(
            create_identity(alumno, f"alumno{i+1}@uah.es")
        )

    # Estudiante UAH (SAML) (sin password, autenticación externa)
    identities.append(
       create_saml_identity(uah_users[0], email="user_uah@uah.es")    
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

    all_users = admins + profesores + alumnos + uah_users

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