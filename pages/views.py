from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, state_choices, bedroom_choices

from listings.models import Listing
from realtors.models import Realtor


# Create your views here.
def index(request):

  listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

  context = {
    'listings': listings,
    'state_choices': state_choices,
    'price_choices': price_choices,
    'bedroom_choices': bedroom_choices,
  }

  return render(request, 'pages/index.html', context)

def about(request):
  realtors = Realtor.objects.order_by('-hire_date')[:3]
  featured = Realtor.objects.all().filter(is_mvp=True)[:1]

  context = {
    'realtors': realtors,
    'featured': featured
  }
  return render(request, 'pages/about.html', context)

