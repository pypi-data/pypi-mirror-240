from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (

    # SystemRole
    path('system-roles/', views.SystemRoleListView.as_view(), name='systemrole_list'),
    path('system-roles/add/', views.SystemRoleEditView.as_view(), name='systemrole_add'),
    path('system-roles/<int:pk>/', views.SystemRoleView.as_view(), name='systemrole'),
    path('system-roles/<int:pk>/edit/', views.SystemRoleEditView.as_view(), name='systemrole_edit'),
    path('system-roles/<int:pk>/delete/', views.SystemRoleDeleteView.as_view(), name='systemrole_delete'),
    path('system-roles/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='systemrole_changelog', kwargs={
        'model': models.SystemRole
    }),
    
    # techrole
    path('tech-roles/', views.TechRoleListView.as_view(), name='techrole_list'),
    path('tech-roles/add/', views.TechRoleEditView.as_view(), name='techrole_add'),
    path('tech-roles/<int:pk>/', views.TechRoleView.as_view(), name='techrole'),
    path('techr-oles/<int:pk>/edit/', views.TechRoleEditView.as_view(), name='techrole_edit'),
    path('tech-roles/<int:pk>/delete/', views.TechRoleDeleteView.as_view(), name='techrole_delete'),
    path('tech-roles/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='techrole_changelog', kwargs={
        'model': models.TechRole
    }),  

)
