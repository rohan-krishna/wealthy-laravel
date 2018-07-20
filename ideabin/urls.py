from django.urls import path
from .views import IdeasListView

app_name='ideabin'

urlpatterns = [
    path('',IdeasListView.as_view()),
]