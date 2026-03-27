# app/core/middleware/auth_middleware.py

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import RedirectResponse

from app.core.security import create_access_token, validate_access_token, validate_refresh_token


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

        # 0. Evitar llamadas a la api
        if path.startswith("/api"):
            return await call_next(request)

        # 🟢 1. Rutas públicas → no tocar
        if any(path.startswith(p) for p in PUBLIC_PATHS):
            return await call_next(request)

        access_token = request.cookies.get("access_token")

        # 🟡 2. No token → login
        if not access_token:
            return RedirectResponse("/login",status_code=302)

        # 🔵 3. Validar access token
        try:
            payload = validate_access_token(access_token)

            request.state.user = {
                "sub": payload.get("sub"),
                "roles": payload.get("roles", []),
                "username": payload.get("username")
            }

            return await call_next(request)

        except:
            # 🔴 4. Intentar refresh automático
            refresh_token = request.cookies.get("refresh_token")

            if not refresh_token:
                return RedirectResponse("/login",status_code=302)

            try:
                payload = validate_refresh_token(refresh_token)

                if payload.get("type") != "refresh":
                    return RedirectResponse("/login",status_code=302)

                # 🔥 generar nuevo access token
                new_access_token = create_access_token({
                    "sub": payload.get("sub"),
                    "roles": payload.get("roles", []),
                    "username": payload.get("username")
                })

                request.state.user = {
                    "sub": payload.get("sub"),
                    "roles": payload.get("roles", []),
                    "username": payload.get("username")
                }

                # 👉 IMPORTANTE: inyectar token nuevo en request
                request.cookies._dict["access_token"] = new_access_token  # hack controlado

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
                return RedirectResponse("/login",status_code=302)