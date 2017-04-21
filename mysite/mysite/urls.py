from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^fantasybumps/', include('fantasybumps.urls')),
    url(r'^admin/', admin.site.urls),
]