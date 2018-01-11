from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Destination,Option
# Create your views here.


def index(request):
    destination_list = Destination.objects.order_by("date")
    return render(request, "travel/index.html", {'destination_list':destination_list})


def detail(request,destination_id):
    place = get_object_or_404(Destination, pk=destination_id)
    return render(request, 'travel/detail.html', {'place': place})


def dates(request, destination_id):
    destination_date = get_object_or_404(Destination, pk=destination_id)
    return render(request, 'travel/dates.html', {'destination_date': destination_date})


def final(request,destination_id):
    return HttpResponse(f"This is the final destination page {destination_id} ")




