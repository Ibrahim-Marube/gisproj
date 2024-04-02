from django.shortcuts import render, redirect
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from ..geoapp.models import Location
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

def location_list(request):
    locations = Location.objects.all()
    return render(request, 'location_list.html', {'locations': locations})

def login_view(request):
    if request.method == 'POST':
        # Add your login logic here
        pass
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def location_search(request):
    user_location = Point(request.GET['longitude'], request.GET['latitude'])
    radius = int(request.GET['radius'])
    locations = Location.objects.filter(coordinates__distance_lte=(user_location, radius))
    locations = locations.annotate(distance=Distance('coordinates', user_location))
    return render(request, 'search_results.html', {'locations': locations})
