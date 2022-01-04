from django.shortcuts import render, get_object_or_404
from .models import IPOProject


def index(request):
    ipo_projects = IPOProject.objects.order_by('-date')[:20]
    for project in ipo_projects:
        project.save()
    return render(request, 'ipos/index.html', {'ipo_projects': ipo_projects})


def detail(request, ipos_id):
    ipos = get_object_or_404(IPOProject, pk=ipos_id)
    return render(request, 'ipos/detail.html', {'ipos': ipos})
