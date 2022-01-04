from django.shortcuts import render, get_object_or_404
from .models import LoanProject


def index(request):
    loan_projects = LoanProject.objects.order_by('-date')[:20]
    for project in loan_projects:
        project.save()
    return render(request, 'loans/index.html', {'loan_projects': loan_projects})


def detail(request, loans_id):
    loans = get_object_or_404(LoanProject, pk=loans_id)
    return render(request, 'loans/detail.html', {'loans': loans})
