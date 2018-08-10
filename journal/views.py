from django.shortcuts import render, redirect
from .forms import EntryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
import json

from django.http import HttpResponse, JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from . models import Entry
# Create your views here.

@login_required
def index(request):
    entries_list = request.user.entries.all()
    paginator = Paginator(entries_list, 10)
    page = request.GET.get('page')
    entries = paginator.get_page(page)

    return render(request, 'journal/index.html', { "entries" : entries })


# Never call this except from the Add New Entry Button
@login_required
def add(request):
    
    entry = Entry.objects.create(user=request.user)

    return redirect('journal:create', pk=entry.pk)

# A Pseudo redirect for creation page, can handle straight traffic too
@login_required
def create(request, pk):
    if request.method == 'GET':
        entry = Entry.objects.get(pk=pk)
        form = EntryForm(instance=entry)
        return render(request, 'journal/add.html', { "entry" : entry, "form" : form })
    else:
        # let's just save the body and title content
        data = request.POST

        entry = Entry.objects.get(pk=pk)
        entry.body = data['body']
        entry.title = data['title']
        entry.save()

        return JsonResponse({ "message" : "Success!" })
    

# When the user submits, this should handle it
@login_required
def store(request, pk):
    entry = Entry.objects.get(pk=pk)

    form = EntryForm(request.POST, instance=entry)

    if form.is_valid():
        entry = form.save(commit=False)
        entry.save()

        return redirect('journal:index')

@login_required
def edit(request, id):
    entry = request.user.entries.get(pk=id)

    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.entry_date = timezone.now()
            entry.save()

            return redirect('journal:index')
    else:
        form = EntryForm(instance=entry)
        return render(request, 'journal/edit.html', { "entry" : entry, "form" : form })


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("journal:index")