from django.shortcuts import render, get_object_or_404
from .models import CarouselAd


def cp_carousel(request):
    carousel_ads = CarouselAd.objects.filter(status='ACTIVE').order_by('-date')
    return {'carousel_ads': carousel_ads}
