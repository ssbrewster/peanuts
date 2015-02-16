from rest_framework import serializers
from .models import Article


class ArticleSerializer(HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username')

    class Meta:
        model = Article
        fields = ('url', 'author', 'title', 'body')
