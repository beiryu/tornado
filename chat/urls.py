from . import handlers

urlpatterns = [
    (r"/messager", handlers.MessagerHandler),
    (r"/chat", handlers.ChatHandler),
    (r"/chat/status", handlers.StatusHandler)
]

