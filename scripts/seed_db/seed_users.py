from app.modules.users.user_model import User


def seed_users(db, roles):
    admins = [
        User(nombre="Admin Principal", activo=True),
        User(nombre="Admin Secundario", activo=True),
    ]

    profesores = [
        User(nombre="Profesor García", activo=True),
        User(nombre="Profesor López", activo=True),
        User(nombre="Profesor Martínez", activo=True),
    ]

    alumnos = [
        User(nombre=f"Alumno {i}", activo=True)
        for i in range(1, 21)
    ]

    uah_users = [
        User(nombre="Usuario UAH Demo", activo=True)
    ]

    all_users = admins + profesores + alumnos + uah_users

    db.add_all(all_users)
    db.commit()

    for u in admins:
        u.roles.append(roles["admin"])

    for u in profesores:
        u.roles.append(roles["profesor"])

    for u in alumnos:
        u.roles.append(roles["estudiante"])

    for u in uah_users:
        u.roles.append(roles["uah_user"])

    db.commit()

    return {
        "admins": admins,
        "profesores": profesores,
        "alumnos": alumnos,
        "uah_users": uah_users
    }