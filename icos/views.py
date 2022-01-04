from django.shortcuts import render, get_object_or_404
from .models import ICOProject


def index(request):
    ico_projects = ICOProject.objects.order_by('-date')[:20]
    for project in ico_projects:
        project.save()
    return render(request, 'icos/index.html', {'ico_projects': ico_projects})


def detail(request, icos_id):
    icos = get_object_or_404(ICOProject, pk=icos_id)
    return render(request, 'icos/detail.html', {'icos': icos})
