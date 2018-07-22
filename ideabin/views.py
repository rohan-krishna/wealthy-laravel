from django.shortcuts import render, redirect
from . models import *
from .forms import IdeaForm

from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (View, 
                                  ListView, 
                                  TemplateView, 
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
# Create your views here.
class IdeaListView(LoginRequiredMixin,ListView):
    model = Idea
    context_object_name = 'ideas'
    template_name = 'ideabin/index.html'

class IdeaDetailView(LoginRequiredMixin,DetailView):
    model = Idea
    context_object_name = 'idea_detail'
    template_name = 'ideabin/idea_detail.html'

class IdeaCreateView(LoginRequiredMixin,CreateView):
    model = Idea
    fields = ('title','body','image')
    template_name = 'ideabin/add.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        self.object.save()

        return super(IdeaCreateView, self).form_valid(form)
    

class IdeaUpdateView(LoginRequiredMixin,UpdateView):
    model = Idea
    fields = ('title','body','image')
    template_name = 'ideabin/edit.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        self.object.save()

        return super(IdeaUpdateView, self).form_valid(form)


class IdeaDeleteView(LoginRequiredMixin,DeleteView):
    model = Idea
    success_url = reverse_lazy("ideabin:index")