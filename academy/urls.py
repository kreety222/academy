from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about, name="about"),
    path('serv/', include('serv.urls')),
    path('styles/', include('styles.urls'))
]

