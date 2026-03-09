from fastapi.templating import Jinja2Templates
from app.web.context import get_template_context

templates = Jinja2Templates(directory="app/templates")

templates.env.globals.update(
    get_template_context=get_template_context
)