# app/core/middleware/auth_middleware.py

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import RedirectResponse

from app.core.security import decode_access_token, create_access_token


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        access_token = request.cookies.get("access_token")

        # 1️⃣ si no hay token → seguir (login etc)
        if not access_token:
            return await call_next(request)

        # 2️⃣ intentar validar access token
        try:
            decode_access_token(access_token)
            return await call_next(request)

        except:
            # 3️⃣ intentar refresh
            refresh_token = request.cookies.get("refresh_token")

            if not refresh_token:
                return RedirectResponse("/login")

            try:
                payload = decode_access_token(refresh_token)

                if payload.get("type") != "refresh":
                    return RedirectResponse("/login")

                # 🔥 generar nuevo access
                new_access_token = create_access_token({
                    "sub": payload.get("sub"),
                    "roles": payload.get("roles", [])
                })

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
                return RedirectResponse("/login")