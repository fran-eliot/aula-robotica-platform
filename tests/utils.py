def login_admin(client):
    return client.post(
        "/login",
        data={
            "email": "admin1@robotica.es",
            "password": "1234"
        },
        follow_redirects=False
    )