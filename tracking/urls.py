from . import handlers

urlpatterns = [
    (r"/history", handlers.HistoryHandler),
    (r"/history/(\w+)", handlers.HistoryHandler),
]

