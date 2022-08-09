from . import handlers

urlpatterns = [
    (r"/device", handlers.DeviceHandler),
    (r"/device/edit/(\w+)", handlers.DeviceEditHandler),
    (r"/device/add", handlers.DeviceEditHandler),
    (r"/device/remove/(\w+)", handlers.DeviceRemoveHandler),
]

