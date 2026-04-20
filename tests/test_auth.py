# tests/test_auth.py
# Este archivo contiene pruebas para la funcionalidad de autenticación de la aplicación.


def test_login_page(client):
    response = client.get("/login")
    assert response.status_code == 200

def test_login_success(client):
    response = client.post(
        "/login",
        data={
            "email": "admin1@robotica.es", 
            "password": "1234"
            },
            follow_redirects=False
    )
    assert response.status_code in (302, 303)  # Redirección después del inicio de sesión exitoso

def test_login_fail(client):
    response = client.post(
        "/login",
        data={
            "email": "fake@test.com", 
            "password": "wrongpassword"
            },
    )
    assert response.status_code == 200  # Sin redirección, se muestra la página de inicio de sesión nuevamente  

def test_mock_login(client):
    response = client.get("/auth/saml/mock", follow_redirects=False)
    assert response.status_code == 302  # Redirección después del inicio de sesión exitoso

