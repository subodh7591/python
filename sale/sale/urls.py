from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^category/', include('category.urls')),
    url(r'^tac/', include('tac.urls')),
    ]
