from . import handlers

urlpatterns = [
    (r"/covid", handlers.CovidHandler),
]

