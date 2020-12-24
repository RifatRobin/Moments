from django.urls import path
from.import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register', views.register, name="register"),
    path('add', views.add, name='add'),
    path('home', views.home, name='home'),
    path('del', views.delete, name="delete"),
]
