from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import HealthEntry
from .forms import HealthEntryForm
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from users.models import HealthEntry

@method_decorator(login_required, name="dispatch")
class HealthEntryListView(ListView):
    model = HealthEntry
    template_name = "app/entry_list.html"
    paginate_by = 20

    def get_queryset(self):
        # only return entries of the current user
        return HealthEntry.objects.filter(user=self.request.user)

@method_decorator(login_required, name="dispatch")
class HealthEntryCreateView(CreateView):
    model = HealthEntry
    form_class = HealthEntryForm
    template_name = "app/entry_form.html"
    success_url = reverse_lazy("entries:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class HealthEntryUpdateView(UpdateView):
    model = HealthEntry
    form_class = HealthEntryForm
    template_name = "app/entry_form.html"

    def get_queryset(self):
        # ownership of the update
        return HealthEntry.objects.filter(user=self.request.user)


@method_decorator(login_required, name="dispatch")

class HealthEntryDeleteView(DeleteView):
    model = HealthEntry
    success_url = reverse_lazy("entries:list")


    def get_queryset(self):
        return HealthEntry.objects.filter(user=self.request.user)

        

