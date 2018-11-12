from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index,name='index'),
    path('show_forms/',views.show_forms,name='show_forms'),
    path('login_succeed/', views.form_login_succeed, name='login_succeed'),
    path('comment_form/',views.comment_form, name='comment_form'),
    path('simple_form/',views.simple_form,name='simple_form'),
]