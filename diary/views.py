from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Entry, Category, Tag
from .forms import EntryForm

@login_required
def entry_list(request):
    entries = Entry.objects.filter(author=request.user).order_by('-created')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'diary/entry_list.html', {'entries': entries, 'categories': categories, 'tags': tags})

@login_required
def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk, author=request.user)
    return render(request, 'diary/entry_detail.html', {'entry': entry})

@login_required
def entry_create(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.save()
            form.save_m2m()
            return redirect('entry_list')
    else:
        form = EntryForm()
    return render(request, 'diary/entry_form.html', {'form': form})

@login_required
def entry_edit(request, pk):
    entry = get_object_or_404(Entry, pk=pk, author=request.user)
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_detail', pk=pk)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'diary/entry_form.html', {'form': form})

@login_required
def entry_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk, author=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('entry_list')
    return render(request, 'diary/entry_confirm_delete.html', {'entry': entry})