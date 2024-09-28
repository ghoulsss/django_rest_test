from rest_framework import generics
from news.serializers import NewsSerializer
from .models import *


class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
