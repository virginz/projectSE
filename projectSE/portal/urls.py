from django.urls import path, include
from . import views, views_admin, admin_procedures

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('admin/home', views_admin.AdminView.as_view(), name='systemadministrator_home'),
    path('admin/home/procedures', admin_procedures.ProcedureView.as_view(), name='systemadministrator_procedures'),
    path('admin/home/add-user/', views_admin.create_user, name='add_user'),
    path('admin/home/add-procedure/', admin_procedures.create_procedure, name='add_procedure'),
    path('admin/home/<int:pk>/edit/', views_admin.UserEditView.as_view(), name='user_edit'),
    path('admin/home/<int:pk>/edit-procedure/', admin_procedures.ProcedureEditView.as_view(), name='procedure_edit'),
    path('admin/home/<int:pk>/delete/', views_admin.UserDeleteView.as_view(), name='user_delete'),
    path('admin/home/<int:pk>/delete-procedure/', admin_procedures.ProcedureDeleteView.as_view(), name='procedure_delete'),
]
