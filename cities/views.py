from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import reverse, redirect, render
from django.urls import reverse_lazy

from .models import City, Mayor, Street
from .forms import CityForm, StreetForm


class IndexView(TemplateView):
    template_name = 'index.html'


class CitiesView(ListView):
    template_name = 'cities/cities.html'
    model = City
    context_object_name = 'cities'

    def get_context_data(self, **kwargs):
        context = super(CitiesView, self).get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        return context


class MayorsView(ListView):
    template_name = 'cities/mayors.html'
    model = Mayor
    context_object_name = 'mayors'


class CityCreateView(CreateView):
    model = City
    form_class = CityForm

    def get_success_url(self):
        return reverse('cities')


class MayorCreateView(CreateView):
    model = Mayor
    fields = ['first_name', 'last_name', 'date_of_birth']

    def get_success_url(self):
        return reverse('mayors')


class MayorDelete(DeleteView):
    model = Mayor
    success_url = reverse_lazy('mayors')


class CityDelete(DeleteView):
    model = City
    success_url = reverse_lazy('cities')


class StreetDelete(DeleteView):
    model = Street
    success_url = reverse_lazy('cities')


class MayorUpdate(UpdateView):
    model = Mayor
    fields = '__all__'
    success_url = reverse_lazy('mayors')


class CityUpdate(UpdateView):
    model = City
    fields = '__all__'
    success_url = reverse_lazy('cities')


class StreetUpdate(UpdateView):
    model = Street
    fields = '__all__'
    success_url = reverse_lazy('cities')


def new_street(request, pk):
    city = City.objects.get(pk=pk)
    print(city.name)
    if request.method == 'POST':
        form = StreetForm(request.POST)
        if form.is_valid():
            street = form.save(commit=False)
            street.city = city
            street.save()
            return redirect('cities')
    else:
        form = StreetForm(None)
    return render(request, 'cities/new_street.html', {'form': form})
