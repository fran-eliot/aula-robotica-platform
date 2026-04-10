# core/middleware/auth_middleware.py
# 🔐 Middleware de autenticación y refresh automático

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import RedirectResponse

from app.core.security import validate_access_token, validate_refresh_token
from app.modules.auth.auth_service import refresh_access_token


PUBLIC_PATHS = [
    "/login",
    "/logout",
    "/refresh",
    "/static",
    "/favicon.ico"
]


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        path = request.url.path

        # 0. Evitar llamadas a la API
        if path.startswith("/api"):
            return await call_next(request)

        # 🟢 1. Rutas públicas
        if any(path.startswith(p) for p in PUBLIC_PATHS):
            return await call_next(request)

        access_token = request.cookies.get("access_token")

        print("COOKIES EN MIDDLEWARE:", request.cookies)

        # 🟡 2. No token → login
        if not access_token:
            return RedirectResponse("/login", status_code=302)

        # 🔵 3. Validar access token
        try:
            payload = validate_access_token(access_token)

            request.state.user = payload

            return await call_next(request)

        except:
            # 🔴 4. Intentar refresh automático
            refresh_token = request.cookies.get("refresh_token")

            if not refresh_token:
                return RedirectResponse("/login", status_code=302)

            try:
                # 🔥 validar refresh token
                refresh_payload = validate_refresh_token(refresh_token)

                # 🔥 generar nuevo access token
                new_access_token = refresh_access_token(refresh_payload)

                # 🔥 decodificar nuevo access token
                new_payload = validate_access_token(new_access_token)

                request.state.user = new_payload

                # 👉 inyectar token en request (hack necesario)
                request.cookies._dict["access_token"] = new_access_token

                response = await call_next(request)

                response.set_cookie(
                    key="access_token",
                    value=new_access_token,
                    httponly=True,
                    samesite="lax",
                    path="/"
                )

                return response

            except:
                return RedirectResponse("/login", status_code=302)