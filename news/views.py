from rest_framework.response import Response
from rest_framework.views import APIView
from news.serializers import NewsSerializer
from .models import *


class NewsAPIView(APIView):
    def get(self, request):
        n = News.objects.all()
        return Response({'news': NewsSerializer(n, many=True).data})

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'news': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'method put not allowed'})

        try:
            instance = News.objects.get(pk=pk)
        except:
            return Response({'error': 'object does not exist'})

        serializer = NewsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'news': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'method delete not allowed'})

        try:
            instance = News.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({'error': 'object does not exist'})

        return Response({"post": "delete post " + str(pk)})