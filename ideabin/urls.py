from django.urls import path
from . import views

from .views import IdeaListView, IdeaDetailView

app_name='ideabin'

urlpatterns = [
    path('',IdeaListView.as_view(), name='index'),
    path('<int:pk>',IdeaDetailView.as_view(), name='detail'),
    path('add/',views.addIdea, name='add'),
]