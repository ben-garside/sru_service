import logging
from . import controllers as Ctrl

log = logging.getLogger(__name__)

async def service(request):
    data = await request.json()
    if "action" in data:
        action = getattr(Ctrl, data["action"])
        data.setdefault("action_param", {})
        result = action(**data["action_param"])
        return result