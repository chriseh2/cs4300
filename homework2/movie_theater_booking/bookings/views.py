from django.shortcuts import render

# Create your views here.

def base_view(request, *args, **kwargs):
    return render(request, 'base.html', {})

def movies_view(request, *args, **kwargs):
    return render(request, 'movie_list.html', {})

def seats_view(request, *args, **kwargs):
    return render(request, 'seat_booking.html', {})

def bookings_view(request, *args, **kwargs):
    return render(request, 'booking_history.html', {})