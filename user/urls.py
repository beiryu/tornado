from . import handlers

urlpatterns = [
    (r"/user", handlers.UserHandler),
    (r"/user/add", handlers.UserEditHandler),
    (r"/user/remove/(\w+)", handlers.UserRemoveHandler),
]

