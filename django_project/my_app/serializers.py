from rest_framework import serializers
from .models import Reporter, Article


class ReporterListSerializer(serializers.ModelSerializer):
    """список репортеров/авторов статей"""

    class Meta:
        model = Reporter
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    """список статей"""

    class Meta:
        model = Article
        fields = '__all__'
