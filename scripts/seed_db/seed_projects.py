# scripts/seed_db/seed_projects.py
# Este archivo define la función para insertar datos de proyectos, tareas y 
# actividades

from random import choice, uniform

from app.modules.projects.project_model import Project
from app.modules.tasks.task_model import Task
from app.modules.activities.activity_model import Activity
from app.modules.users.user_model import User


def seed_projects(db):
    print("📁 Seeding projects...")

    if db.query(Project).count() > 0:
        print("⚠️ Projects ya inicializados")
        return

    # =====================================================
    # USUARIOS
    # =====================================================
    users = db.query(User).all()

    if not users:
        print("⚠️ No hay usuarios. Ejecuta seed_users primero.")
        return

    admin = db.query(User).filter_by(
        nombre="Admin Principal"
    ).first()

    profesor = db.query(User).filter_by(
        nombre="Profesor García"
    ).first()

    alumno1 = db.query(User).filter_by(
        nombre="Alumno 1"
    ).first()

    alumno2 = db.query(User).filter_by(
        nombre="Alumno 2"
    ).first()

    alumno3 = db.query(User).filter_by(
        nombre="Alumno 3"
    ).first()

    # fallback por si no existen
    admin = admin or users[0]
    profesor = profesor or users[0]
    alumno1 = alumno1 or users[0]
    alumno2 = alumno2 or users[0]
    alumno3 = alumno3 or users[0]

    team_users = [
        admin,
        profesor,
        alumno1,
        alumno2,
        alumno3,
    ]

    # =====================================================
    # PROYECTOS
    # =====================================================
    projects_data = [
        {
            "name": "Robot Seguidor de Línea",
            "description": "Robot autónomo con sensores IR para circuitos.",
            "status": "Activo",
            "created_by": admin.id_usuario,
        },
        {
            "name": "Brazo Robótico Inteligente",
            "description": "Brazo robótico con servomotores y control preciso.",
            "status": "Activo",
            "created_by": profesor.id_usuario,
        },
        {
            "name": "Drone Educativo",
            "description": "Drone modular para aprendizaje STEM.",
            "status": "Activo",
            "created_by": profesor.id_usuario,
        },
        {
            "name": "Estación Meteorológica IoT",
            "description": "Sensores conectados para monitorización ambiental.",
            "status": "Finalizado",
            "created_by": admin.id_usuario,
        },
        {
            "name": "Coche Autónomo Mini",
            "description": "Vehículo autónomo con visión básica.",
            "status": "Activo",
            "created_by": admin.id_usuario,
        },
    ]

    projects = []

    for item in projects_data:
        project = Project(**item)
        db.add(project)
        projects.append(project)

    db.commit()

    for project in projects:
        db.refresh(project)

    print(f"✅ {len(projects)} proyectos creados")

    # =====================================================
    # TAREAS
    # =====================================================
    tasks_templates = {
        "Robot Seguidor de Línea": [
            ("Diseño del chasis", "Estructura base del robot", "Completada", "Alta"),
            ("Cableado sensores", "Conectar sensores IR", "En progreso", "Alta"),
            ("Programación navegación", "Lógica de seguimiento", "Pendiente", "Alta"),
        ],
        "Brazo Robótico Inteligente": [
            ("Montaje estructura", "Montaje físico del brazo", "Completada", "Media"),
            ("Configurar servos", "Calibración de movimientos", "En progreso", "Alta"),
            ("Control por joystick", "Interfaz manual", "Pendiente", "Media"),
        ],
        "Drone Educativo": [
            ("Montar frame", "Ensamblado principal", "Completada", "Alta"),
            ("Pruebas motores", "Validar hélices y ESC", "Pendiente", "Alta"),
            ("Telemetría", "Enviar datos al panel", "Pendiente", "Media"),
        ],
        "Estación Meteorológica IoT": [
            ("Sensores clima", "Integración sensores", "Completada", "Media"),
            ("Dashboard web", "Visualización de datos", "Completada", "Media"),
        ],
        "Coche Autónomo Mini": [
            ("Montaje ruedas", "Base mecánica", "En progreso", "Media"),
            ("Detección obstáculos", "Sensores ultrasónicos", "Pendiente", "Alta"),
            ("Control velocidad", "PWM motores", "Pendiente", "Media"),
        ],
    }

    tasks = []

    for project in projects:
        templates = tasks_templates.get(project.name, [])

        for name, desc, status, priority in templates:
            assigned_user = choice(team_users)

            task = Task(
                project_id=project.id_project,
                name=name,
                description=desc,
                status=status,
                priority=priority,
                assigned_user_id=assigned_user.id_usuario,
            )

            db.add(task)
            tasks.append(task)

    db.commit()

    for task in tasks:
        db.refresh(task)

    print(f"✅ {len(tasks)} tareas creadas")

    # =====================================================
    # ACTIVIDADES
    # =====================================================
    activity_templates = [
        "Investigación inicial",
        "Montaje componentes",
        "Cableado interno",
        "Programación módulo",
        "Pruebas funcionales",
        "Corrección errores",
        "Optimización rendimiento",
        "Documentación técnica",
        "Validación final",
        "Demo interna",
    ]

    activities = []

    for task in tasks:
        num_activities = choice([2, 3, 4])

        for i in range(num_activities):
            user = choice(team_users)

            activity = Activity(
                name=activity_templates[i],
                description=f"{activity_templates[i]} de la tarea {task.name}",
                status=choice(
                    [
                        "Pendiente",
                        "En progreso",
                        "Completada",
                    ]
                ),
                task_id=task.id_task,
                user_id=user.id_usuario,
                time_spent=round(uniform(0.5, 4.5), 1),
            )

            db.add(activity)
            activities.append(activity)

    db.commit()

    print(f"✅ {len(activities)} actividades creadas")
    print("🚀 Seed projects PRO completado")