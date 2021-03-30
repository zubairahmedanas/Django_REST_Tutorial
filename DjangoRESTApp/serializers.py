

from DjangoRESTApp.models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    authorname = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=50)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.authorname = validated_data.get('authorname', instance.authorname)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('title', instance.date)
        instance.save()
        return instance
