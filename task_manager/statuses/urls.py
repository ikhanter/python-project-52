from django.urls import path
from . import views


urlpatterns = [
    path('', views.StatusesIndexView.as_view(), name='statuses_index'),
    path('create/', views.StatusesCreateView.as_view(), name='statuses_create'),  # noqa: 501
    path('<int:pk>/update/', views.StatusesUpdateView.as_view(), name='statuses_update'),  # noqa: 501
    path('<int:pk>/delete/', views.StatusesDeleteView.as_view(), name='statuses_delete'),  # noqa: 501
]
