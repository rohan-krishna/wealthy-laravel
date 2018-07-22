from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('settings/',views.settings,name='settings'),
    path('set_password/',views.set_password,name='set_password'),
]