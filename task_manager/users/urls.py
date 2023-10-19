from django.urls import path, include
from . import views


urlpatterns = [
    path('create/', views.UsersCreateView.as_view(), name='users_create'),
    path('users/<int:pk>/update/', views.UsersUpdateView.as_view(), name='users_update'),
    path('users/<int:pk>/delete/', views.UsersDeleteView.as_view(), name='users_delete'),
    path('', views.UsersIndexView.as_view(), name='users_index'),
]