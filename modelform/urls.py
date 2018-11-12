from django.urls import path
from . import views

app_name = 'modelform'
urlpatterns = [
    path('register/',views.user_register,name='user_register'),
    path('register_fail/',views.register_fail,name='register_fail'),
    path('register_success/',views.register_success,name='register_success'),
    path('login/',views.user_login,name='user_login'),
    path('index/',views.user_index,name='user_index'),
    path('logout/',views.user_logout,name='user_logout'),
]