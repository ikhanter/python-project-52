from . import views
from django.urls import path


urlpatterns = [
    path('<int:pk>/update/', views.TasksUpdateView.as_view(), name='tasks_update'),  # noqa: 501
    path('<int:pk>/delete/', views.TasksDeleteView.as_view(), name='tasks_delete'),  # noqa: 501
    path('<int:pk>/', views.TasksShowView.as_view(), name='tasks_show'),
    path('create/', views.TasksCreateView.as_view(), name='tasks_create'),
    path('', views.TasksIndexView.as_view(), name='tasks_index'),
]
