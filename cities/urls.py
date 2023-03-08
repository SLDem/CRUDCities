from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(template_name='cities/index.html'), name='index'),
    path('cities/', views.CitiesView.as_view(template_name='cities/cities.html'), name='cities'),
    path('create_city/', views.CityCreateView.as_view(template_name='cities/new_city.html'), name='create_city'),
    path('mayors/', views.MayorsView.as_view(template_name='cities/mayors.html'), name='mayors'),
    path('create_mayor/', views.MayorCreateView.as_view(template_name='cities/new_mayor.html'), name='create_mayor'),
    path('new_street/<int:pk>', views.new_street, name='new_street'),
    path('delete_mayor/<int:pk>', views.MayorDelete.as_view(), name='delete_mayor'),
    path('delete_city/<int:pk>', views.CityDelete.as_view(), name='delete_city'),
    path('delete_street/<int:pk>', views.StreetDelete.as_view(), name='delete_street'),
    path('edit_mayor/<int:pk>', views.MayorUpdate.as_view(), name='edit_mayor'),
    path('edit_city/<int:pk>', views.CityUpdate.as_view(), name='edit_city'),
    path('edit_street/<int:pk>', views.StreetUpdate.as_view(), name='edit_street'),
]
