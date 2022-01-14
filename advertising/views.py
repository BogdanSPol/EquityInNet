# from django.shortcuts import render, get_object_or_404
# from .models import CarouselAds
#
#
# def index(request):
#     carousel_ads = CarouselAds.objects.all()
# #    for ad in carousel_ads:
# #        ad.save()
#     return render(request, 'advertising/index.html', {'carousel_ads': carousel_ads})
#
#
# def detail(request, equities_slug: str):
#     ads = get_object_or_404(CarouselAds, slug=ads_slug)
#     return render(request, 'equities/index.html', {'ads': ads})