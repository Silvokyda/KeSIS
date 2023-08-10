from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path('dashboard/'       , views.index,  name='dash'),
  path('tables/', views.tables, name='tables'),
]
