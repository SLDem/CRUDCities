from django.shortcuts import render, redirect

from .forms import SignupForm
from user_profile.models import User


def signup(request):
    title = 'Signup'
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data.get('password1')
            name = form.cleaned_data['name']
            user.is_active = False
            user = User.objects.create(email=user.email, password=raw_password, name=name)
            user.set_password(raw_password)
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'authentication/custom_signup.html', {'form': form, 'title': title})
