from django.urls import path
from . import views
urlpatterns=[
    path('style/', views.style, name='style')
]
