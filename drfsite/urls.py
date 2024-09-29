from django.contrib import admin
from django.urls import path
from news.views import NewsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/newslist/', NewsAPIView.as_view()),
    path('api/v1/newslist/<int:pk>/', NewsAPIView.as_view()),
]
