from . import routes

def setup(app):
    app.router.add_route("POST", "/service", routes.service)