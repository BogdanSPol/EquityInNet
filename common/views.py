from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from common.models import Currency, SectorChoice


def pagination(table_set, page, paginate_by):
    paginator = Paginator(table_set, paginate_by)
    try:
        page_obj = paginator.get_page(page)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


def currencies_list():
    return Currency.objects.all()


def sectors_list():
    return SectorChoice.objects.all()
