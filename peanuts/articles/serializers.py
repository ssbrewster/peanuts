from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username', read_only='True')

    class Meta:
        model = Article
        fields = ('url', 'author', 'title', 'body')
