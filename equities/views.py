from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import EquityProject


def index(request):
    equity_projects = EquityProject.objects.filter(~Q(is_active='ENDED')).order_by('-add_date_time')[:20]
    for project in equity_projects:
        project.save()
    return render(request, 'equities/index.html', {'equity_projects': equity_projects})


def detail(request, equities_slug: str):
    equities = get_object_or_404(EquityProject, slug=equities_slug)
    return render(request, 'equities/detail.html', {'equities': equities})
