from django.urls import path, include
from . import views, views_admin

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('admin/home', views_admin.AdminView.as_view(), name='systemadministrator_home'),
    path('admin/home/add-user/', views_admin.create_user, name='add_user'),
]
