from django.urls import path

from app import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('contact/',views.contact,name='contact'),
]
