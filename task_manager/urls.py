"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('users/<int:pk>/update/', views.UsersUpdateView.as_view(), name='users_update'),
    # path('users/<int:pk>/delete/', views.UsersDeleteView.as_view(), name='users_delete'),
    path('users/create/', views.UsersCreateView.as_view(), name='users_create'),
    # path('users/', views.UsersIndexView.as_view(), name='users_index'),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', views.IndexView.as_view(), name='index'),
]
