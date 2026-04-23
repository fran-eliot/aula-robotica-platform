from app.db.session import SessionLocal
from scripts.seed_db.seed_audit import seed_audit
from scripts.seed_db.seed_identities import seed_identities
from scripts.seed_db.seed_roles import seed_roles
from scripts.seed_db.seed_users import seed_users


def run():
    db = SessionLocal()

    print("🌱 Iniciando seed...")

    roles, permissions = seed_roles(db)
    users = seed_users(db, roles)
    seed_identities(db, users)
    seed_audit(db, users)

    db.close()

    print("✅ Seed completado correctamente")


if __name__ == "__main__":
    run()