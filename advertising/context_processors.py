from .models import CarouselAd


def cp_carousel(request):
    carousel_ads = CarouselAd.objects.filter(status='ACTIVE').order_by('-date')
    return {'carousel_ads': carousel_ads}
