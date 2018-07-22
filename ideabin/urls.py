from django.urls import path
from . import views

from .views import IdeaListView, IdeaDetailView, IdeaCreateView, IdeaUpdateView, IdeaDeleteView

app_name='ideabin'

urlpatterns = [
    path('',IdeaListView.as_view(), name='index'),
    path('<int:pk>',IdeaDetailView.as_view(), name='detail'),
    path('add/',IdeaCreateView.as_view(), name='add'),
    path('edit/<int:pk>',IdeaUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>',IdeaDeleteView.as_view(), name='delete'),
]