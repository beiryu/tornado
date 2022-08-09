from . import handlers

urlpatterns = [
    (r'/', handlers.DashboardHandler),
    (r'/login', handlers.LoginHandler),
    (r'/logout', handlers.LogoutHandler), 
]