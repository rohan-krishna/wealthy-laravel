from django.shortcuts import render, redirect
from . models import *
from .forms import IdeaForm

from django.contrib.auth.decorators import login_required

from django.views.generic import (View, 
                                  ListView, 
                                  TemplateView, 
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
# Create your views here.
@login_required
def index(request):
    ideas = request.user.ideas.all
    return render(request, 'ideabin/index.html', { 'ideas' : ideas })


@login_required
def addIdea(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.user = request.user
            idea.save()
            return redirect('ideabin:index')
    else:
        return render(request, 'ideabin/add.html', { "form" : IdeaForm })


class IdeaListView(ListView):
    model = Idea
    context_object_name = 'ideas'
    template_name = 'ideabin/index.html'

class IdeaDetailView(DetailView):
    model = Idea
    context_object_name = 'idea_detail'
    template_name = 'ideabin/idea_detail.html'

class IdeaCreateView(CreateView):
    model = Idea
    fields = ('title','body')
    template_name = 'ideabin/add.html'


