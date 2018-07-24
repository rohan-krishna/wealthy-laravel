from django.urls import path
from . import views
from .views import EntryDeleteView


app_name='journal'

urlpatterns = [
    path('',views.index, name='index'),
    path('add-new/',views.add, name='add'),
    path('transact/<int:pk>',views.create, name='create'),
    path('store/<int:pk>',views.store, name='store'),
    path('edit/<int:id>',views.edit, name='edit'),
    path('delete/<int:pk>',EntryDeleteView.as_view(), name='delete'),
]