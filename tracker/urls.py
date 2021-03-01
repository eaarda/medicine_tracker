from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.main, name="main"),
    path('account/', views.account, name="account"),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
