from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import EquityProject
from common.views import pagination, currencies_list, sectors_list
from datetime import date, timedelta


def index(request):
    paginate_by = request.GET.get('paginate_by') or 5
    page = request.GET.get('page')
    equity_projects = EquityProject.objects.filter(~Q(is_active='ENDED')).order_by('-add_date_time')
    for project in equity_projects:
        project.save()
    page_obj = pagination(equity_projects, page, paginate_by)

    return render(request, 'equities/index.html', {
        'page_obj': page_obj,
        'currencies': currencies_list(),
        'sectors': sectors_list(),
        'paginate_by': paginate_by,
    })


def filters(request):
    page = request.GET.get('page')

    paginate_by = request.GET.get('paginate_by') or 5

    currency_get = request.GET.getlist('currency')
    if not currency_get:
        currency_get = currencies_list()

    sector_get = request.GET.getlist('sector')
    if not sector_get:
        sector_get = sectors_list()

    score_get = request.GET.get('score').split(sep=";")
    score_get_min = score_get[0]
    score_get_max = score_get[1]

    days_to_go_get = request.GET.get('days_to_go').split(sep=";")
    date_to_go_get_from = date.today() + timedelta(days=int(days_to_go_get[0]))
    date_to_go_get_to = date.today() + timedelta(days=int(days_to_go_get[1]))

    min_invest_get = request.GET.get('min_invest').split(sep=";")
    min_invest_get_min = min_invest_get[0]
    min_invest_get_max = min_invest_get[1]

    raised_get = request.GET.get('raised').split(sep=";")
    raised_get_min = raised_get[0]
    raised_get_max = raised_get[1]

    equity_projects_queryset = EquityProject.objects.filter(
        ~Q(is_active='ENDED'),
        Q(currency_id__in=currency_get),
        Q(sector_choice_id__in=sector_get),
        Q(score__gte=score_get_min) & Q(score__lte=score_get_max),
        Q(end_date__gte=date_to_go_get_from) & Q(end_date__lte=date_to_go_get_to),
        Q(min_investment_amount__gte=min_invest_get_min) & Q(min_investment_amount__lte=min_invest_get_max)
    ).order_by('-add_date_time')

    equity_projects_queryset_filtered = []
    for eq in equity_projects_queryset:
        per = eq.invested * 100 / eq.round_money
        if (per >= float(raised_get_min)) and (per <= float(raised_get_max)):
            equity_projects_queryset_filtered.append(eq)

    page_obj = pagination(equity_projects_queryset_filtered, page, paginate_by)

    return render(request, 'equities/filters.html', {
        'page_obj': page_obj,
        'currencies': currencies_list(),
        'sectors': sectors_list(),
        'paginate_by': paginate_by,
    })


def detail(request, equities_slug: str):
    equities = get_object_or_404(EquityProject, slug=equities_slug)
    return render(request, 'equities/detail.html', {'equities': equities})
