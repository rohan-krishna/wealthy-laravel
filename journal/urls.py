from django.urls import path
from . import views

app_name='journal'

urlpatterns = [
    path('',views.index, name='index'),
    path('add-new/',views.add, name='add'),
    path('edit/<int:id>',views.edit, name='edit'),
]