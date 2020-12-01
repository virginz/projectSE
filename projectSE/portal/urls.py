from django.urls import path, include
from . import views, views_admin, admin_procedures
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/home/', login_required(views_admin.AdminView.as_view()), name='systemadministrator_home'),
    path('admin/home/procedures', login_required(admin_procedures.ProcedureView.as_view()), name='systemadministrator_procedures'),
    path('admin/home/add-user/', views_admin.create_user, name='add_user'),
    path('admin/home/add-procedure/', admin_procedures.create_procedure, name='add_procedure'),
    path('admin/home/<int:pk>/edit-procedure/', login_required(admin_procedures.ProcedureEditView.as_view()), name='procedure_edit'),
    path('admin/home/<int:pk>/delete/', login_required(views_admin.UserDeleteView.as_view()), name='user_delete'),
    path('admin/home/<int:pk>/delete-procedure/', login_required(admin_procedures.ProcedureDeleteView.as_view()), name='procedure_delete'),
]
