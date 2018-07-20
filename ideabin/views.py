from django.shortcuts import render
from django.views.generic import ListView
from . models import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class IdeasListView(LoginRequiredMixin, ListView):
    
    model = Idea

    def get_queryset(self):
        return Idea.objects.filter(user=self.request.user)