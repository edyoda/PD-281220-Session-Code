from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=100)
    # content = serializers.CharField(min_length=10)
    # author = serializers.CharField(max_length=100)
    # email = serializers.EmailField()
    # date = serializers.DateField()
    #
    # def create(self, validated_data):
    #     return Article.objects.create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.content = validated_data.get("content", instance.content)
    #     instance.author = validated_data.get("title", instance.author)
    #     instance.email = validated_data.get("title", instance.email)
    #     instance.date = validated_data.get("date", instance.date)
    #     instance.save()
    class Meta:
        model = Article
        fields = "__all__"