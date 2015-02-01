from django.forms import widgets
from rest_framework import serializers
from .models import Article


class ArticleSerializer(HyperLinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='author-detail', read-only='True')

    class Meta:
        model = Article
        fields = ('url', 'author', 'title', 'body')
