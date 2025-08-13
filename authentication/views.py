from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import HealthEntry
from .forms import HealthEntryForm

@login_required
def entry_list(request):
    entries = HealthEntry.objects.filter(user=request.user)
    return render (request, 'app/entry_list.html', {'entries':entries})


@login_required
def entry_create(request):
    if request.method == 'POST':
        form = HealthEntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('entry_list')
    else:
        form = HealthEntryForm()
    return render(request, 'app/entry_form.html', {'form':form})


@login_required

def entry_edit(request, pk):
    entry = get_object_or_404(HealthEntry, pk=pk)
    if entry.user != request.user:
        return HttpResponseForbidden("You dont have permission to edit this entry")
    if request.method == 'POST':
        form = HealthEntryForm(request.POST,  request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
        else:
            form = HealthEntryForm(instance=entry)
        return render(request, 'app/entry_form.html', {'form':form})


@login_required
def entry_delete(request, pk):
    entry = get_object_or_404(HealthEntry, pk=pk)
    if entry.user != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        entry.delete()
        return redirect('entry_list')
    return render (request, 'app/entry_confirm_delet.html', {'entry':entry})

        