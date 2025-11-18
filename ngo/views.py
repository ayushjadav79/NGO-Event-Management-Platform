from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NGORegistrationForm
from .models import NGO
from django.contrib.auth.decorators import login_required

@login_required
def register_ngo(request):
    if request.method == 'POST':
        form = NGORegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'NGO registered successfully!')
            return redirect('ngo_list')
    else:
        form = NGORegistrationForm()
    return render(request, 'ngo/register.html', {'form': form})

@login_required
def ngo_list(request):
    ngos = NGO.objects.all()
    return render(request, 'ngo/list.html', {'ngos': ngos})