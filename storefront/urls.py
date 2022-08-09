from admin.urls import urlpatterns as admin_urls
from device.urls import urlpatterns as device_urls
from user.urls import urlpatterns as user_urls
from tracking.urls import urlpatterns as tracking_urls
from chat.urls import urlpatterns as chat_urls
from covid.urls import urlpatterns as covid_urls

urlpatterns = device_urls \
            + admin_urls \
            + user_urls \
            + tracking_urls \
            + chat_urls \
            + covid_urls

