from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from DjangoRESTApp.models import Article
from DjangoRESTApp.serializers import ArticleSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer


class Articlelist(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'article.html'
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response({'Article' : article})

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):
    def get_objects(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.Does_Not_Exist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        article = self.get_objects(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self,request, id):
        article = self.get_objects(id)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



    def delete(self):
        article = self.get_objects(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""

@csrf_exempt
def articlelist(request):
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def articledetail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except article.DoesNotExist:
        return JsonResponse(status=404)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    if request.method == 'DELETE':
        article.delete()
        return JsonResponse(status=204)
        
        
"""
