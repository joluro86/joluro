from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.list_users, name='list_users'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('users/change_status/<int:user_id>/', views.change_user_status, name='change_user_status'),
]
