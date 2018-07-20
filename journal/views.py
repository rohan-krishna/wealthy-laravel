from django.shortcuts import render, redirect
from .forms import EntryForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    entries = request.user.entries.all
    return render(request, 'journal/index.html', { "entries" : entries })

@login_required
def add(request):
    
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('journal:index')
    else:
        return render(request, 'journal/add.html', { "form" : EntryForm })

@login_required
def edit(request, id):
    entry = request.user.entries.get(pk=id)

    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()

            return redirect('journal:index')
    else:
        form = EntryForm(instance=entry)
        return render(request, 'journal/edit.html', { "entry" : entry, "form" : form })
