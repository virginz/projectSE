from django.urls import path, include
from . import views, views_admin_users, view_admin_procedures, view_planner_activity, view_planner_assign
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
    path('planner/home/assign-activity?pk<int:pk>&week=<week>', view_planner_assign.AssignView, name='assign_activity'),
    path('planner/home/assign-activity', view_planner_assign.AssignView, name='assign_activity'),
    path('planner/home/slot-activity?pkActivity=<int:pkAct>&pkMaintainer=<int:pkMain>&day=<int:day>', view_planner_assign.ViewAvailabily, name='availability_slot'),
    path('planner/home/slot-activity', view_planner_assign.ViewAvailabily, name='availability_slot'),
    path('planner/home/actitivy-assigned', view_planner_activity.ActivityAssigned.as_view(), name='activity_assigned'),
    path('planner/home/slot-assigned/<int:pkAss>/<int:pkAct>/<int:day>/<int:maintainer>/', view_planner_assign.AssignSlot8_9, name='slot8_9'),
    path('planner/home/slot-assigned/<int:pkAss>/<int:pkAct>/<int:day>/<int:maintainer>/', view_planner_assign.AssignSlot9_10, name='slot9_10'),
    path('planner/home/slot-assigned/<int:pkAss>/<int:pkAct>/<int:day>/<int:maintainer>/', view_planner_assign.AssignSlot10_11, name='slot10_11'),
    path('planner/home/slot-assigned/<int:pkAss>/<int:pkAct>/<int:day>/<int:maintainer>/', view_planner_assign.AssignSlot11_12, name='slot11_12'),
    path('planner/home/slot-assigned/<int:pkAss>/<int:pkAct>/<int:day>/<int:maintainer>/', view_planner_assign.AssignSlot14_15, name='slot14_15'),
    path('planner/home/slot-assigned/<int:pkAss>/<int:pkAct>/<int:day>/<int:maintainer>/', view_planner_assign.AssignSlot15_16, name='slot15_16'),
    path('planner/home/slot-assigned/<int:pkAss>/<int:pkAct>/<int:day>/<int:maintainer>/', view_planner_assign.AssignSlot16_17, name='slot16_17'),

    
]
