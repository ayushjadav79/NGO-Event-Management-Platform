from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import EventCreationForm
from .models import Event
from django.contrib.auth.decorators import login_required

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event added successfully!')
            return redirect('event_list_admin')
    else:
        form = EventCreationForm()
    return render(request, 'events/add.html', {'form': form})

@login_required
def event_list_admin(request):
    events = Event.objects.select_related('ngo').all()
    return render(request, 'events/list_admin.html', {'events': events})

def public_event_list(request):
    events = Event.objects.select_related('ngo').all().order_by('-date_time')

    city = request.GET.get('city', '').strip()
    state = request.GET.get('state', '').strip()

    if city:
        events = events.filter(location_city__iexact=city)
    if state:
        events = events.filter(location_state__iexact=state)

    return render(request, 'events/public_list.html', {
        'events': events,
        'city': city,
        'state': state,
    })

def event_detail(request, pk):
    event = get_object_or_404(Event.objects.select_related('ngo'), pk=pk)
    return render(request, 'events/detail.html', {'event': event})

@login_required
def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventCreationForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated!')
            return redirect('event_list_admin')
    else:
        form = EventCreationForm(instance=event)
    return render(request, 'events/edit.html', {'form': form, 'event': event})

@login_required
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted.')
        return redirect('event_list_admin')
    return render(request, 'events/delete.html', {'event': event})