from django.forms import ModelForm

from .models import City, Mayor, Street


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields['mayor'].queryset = Mayor.objects.filter(city__isnull=True)


class StreetForm(ModelForm):
    class Meta:
        model = Street
        fields = ['name']
