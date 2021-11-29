from django.urls import path
from . import views
urlpatterns=[
    path('Register/', views.fnreg, name='register')
]