from django.shortcuts import render
from .models import Article, Reporter
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ReporterListSerializer, ArticleListSerializer

# -------------------------------------------------------------------
# ----------------------------Вьюхи для API--------------------------
# -------------------------------------------------------------------


class ReporterListView(APIView):
    """вывод списка репортеров"""

    def get(self, request):
        reporters = Reporter.objects.filter()
        serializer = ReporterListSerializer(reporters, many=True)
        return Response(serializer.data)


class ReporterListOfIdViews(APIView):
    """вывод авторов по ID"""

    def get(self, request, id):
        reporters = Reporter.objects.filter(id=id)
        serializer = ReporterListSerializer(reporters, many=True)
        return Response(serializer.data)




class ArticleListViewYears(APIView):
    """вывод списка статей по ГОДАМ"""

    def get(self, request, year):
        articles = Article.objects.filter(pub_date__year=year)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)



class ArticleListView(APIView):
    """вывод списка ВСЕХ статей """


    def get(self, request):
        articles = Article.objects.filter()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)






# -------------------------------------------------------------------
# ----------------------------Вьюхи для сайта------------------------
# -------------------------------------------------------------------

def start(request):
    return render(request, 'index.html')



def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'year_archive.html', context)


def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'year_archive.html', context)


def article_detail(request, year, month, pk):
    a_list = Article.objects.filter(pub_date__year=year, pub_date__month=month, id=pk)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'year_archive.html', context)


def article_id(request, id):
    a_list = Article.objects.filter(id=id)
    context = {'article_list': a_list}
    return render(request, 'year_archive.html', context)



