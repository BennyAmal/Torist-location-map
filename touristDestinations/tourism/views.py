from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from rest_framework import generics, filters
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .forms import destinationForm
import requests


# Create your views here.

class DestinationCreateView(generics.CreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes=[AllowAny]

class DestinationRetrieveView(generics.RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes=[AllowAny]

class DestinationUpdateView(generics.UpdateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes=[AllowAny]

class DestinationDestroyView(generics.DestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes=[AllowAny]

class DestinationSearchView(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query')
        if query:
            return Destination.objects.filter(place_name__icontains=query)
        else:
            return Destination.objects.none()  # Return an empty queryset if no query provided
        

#home
def home(request):
    return render(request, 'home.html')

# django connecting

def createDestination(request):
    if request.method == 'POST':
        form = destinationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                api_url = 'http://127.0.0.1:8000/api/destinations/create/'  # Adjust the API URL
                data = form.cleaned_data

                # Make a request to the API
                response = requests.post(api_url, data=data, files={'image': request.FILES['image']})
                
                if response.status_code == 400:
                    messages.success(request, 'Destination added Successfully')
                else:
                    messages.error(request, f'Error {response.status_code}')

            except requests.RequestException as e:  # Catch RequestException
                messages.error(request, f'Error during API request: {str(e)}')

        else:
            messages.error(request, 'Form is not valid')

    else:
        form = destinationForm()

    return render(request, 'createPage.html', {'form': form})


def display_destinations(request):
    # Get all destinations initially
    destinations = Destination.objects.all()

    # Check if a search query is provided in the URL parameters
    query = request.GET.get('query')
    if query:
        # Filter destinations based on the search query
        destinations = destinations.filter(place_name__icontains=query)

    return render(request, 'showcase.html', {'destinations': destinations})


def update_destination(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    
    if request.method == 'POST':
        form = destinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('showcase')  # Redirect to destination detail page after successful update
    else:
        form = destinationForm(instance=destination)
    
    return render(request, 'updatePage.html', {'form': form})