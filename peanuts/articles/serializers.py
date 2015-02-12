from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='author-detail', read_only='True')

    class Meta:
        model = Article
        fields = ('url', 'author', 'title', 'body')
