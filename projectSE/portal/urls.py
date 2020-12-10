from django.urls import path, include
from . import views, views_admin_users, view_admin_procedures, view_planner_activity
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/home/', login_required(views_admin_users.AdminView.as_view()), name='systemadministrator_home'),
    path('admin/home/procedures', login_required(view_admin_procedures.ProcedureView.as_view()), name='systemadministrator_procedures'),
    path('admin/home/add-user/', views_admin_users.create_user, name='add_user'),
    path('admin/home/add-single-user/', views_admin_users.create_single_user, name='add_single_user'),
    path('admin/home/add-procedures/', view_admin_procedures.create_procedure, name='add_procedure'),
    path('admin/home/add-procedure/', login_required(view_admin_procedures.ProcedureCreateView.as_view()), name='add_one_procedure'),
    path('admin/home/<int:pk>/edit-procedure/', login_required(view_admin_procedures.ProcedureEditView.as_view()), name='procedure_edit'),
    path('admin/home/<int:pk>/delete-user/', login_required(views_admin_users.UserDeleteView.as_view()), name='user_delete'),
    path('admin/home/<int:pk>/delete-procedure/', login_required(view_admin_procedures.ProcedureDeleteView.as_view()), name='procedure_delete'),
    path('admin/home/<int:pk>/edit-user/', login_required(views_admin_users.UserEditView.as_view()), name='user_edit'),
    path('planner/home/', login_required(view_planner_activity.PlannerView.as_view()), name='planner_home'),
    path('planner/home?week=<week>', login_required(view_planner_activity.PlannerView.as_view()), name='planner_home'),
    path('planner/home/add-activity/', login_required(view_planner_activity.ActivityCreateView.as_view()), name='add_activity'),
    path('planner/home/<int:pk>/delete-activity/', login_required(view_planner_activity.PlannerDeleteView.as_view()), name='activity_delete'),
    path('planner/home/<int:pk>/edit-activity/', login_required(view_planner_activity.ActivityEditView.as_view()), name='activity_edit'),
    path('planner/home/<int:pk>/verify-information-activity/', login_required(view_planner_activity.VerifyActivityView.as_view()), name='verify_activity'),
]
