from django.urls import path
from . import views


urlpatterns = [
    path('', views.LabelsIndexView.as_view(), name='labels_index'),
    path('create/', views.LabelsCreateView.as_view(), name='labels_create'),
    path('<int:pk>/update/', views.LabelsUpdateView.as_view(), name='labels_update'),  # noqa: 501
    path('<int:pk>/delete/', views.LabelsDeleteView.as_view(), name='labels_delete'),  # noqa: 501
]
