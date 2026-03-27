ROLE_PERMISSIONS = {
    "admin": [
        "users:create",
        "users:read",
        "users:update",
        "users:delete",
        "roles:assign"
        "dashboard:view"
    ],
    "profesor": [
        "students:read",
        "students:update"
        "dashboard:view"
    ],
    "estudiante": [
        "profile:view"
    ]
}