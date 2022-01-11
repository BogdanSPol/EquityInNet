from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import EquityProject


def index(request):
    paginate_by = request.GET.get('paginate_by', 1) or 1
    equity_projects = EquityProject.objects.filter(~Q(is_active='ENDED')).order_by('-add_date_time')
    for project in equity_projects:
        project.save()
    paginator = Paginator(equity_projects, paginate_by)
    page = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'equities/index.html', {'page_obj': page_obj, 'paginate_by': paginate_by})


def detail(request, equities_slug: str):
    equities = get_object_or_404(EquityProject, slug=equities_slug)
    return render(request, 'equities/detail.html', {'equities': equities})
