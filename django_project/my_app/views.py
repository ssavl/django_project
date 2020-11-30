from django.shortcuts import render

# Create your views here.

from .models import Article


def start(request):
    x = render(request, 'index.html')
    print(x)
    return x


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'year_archive.html', context)


def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'year_archive.html', context)


def article_detail(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'year_archive.html', context)

