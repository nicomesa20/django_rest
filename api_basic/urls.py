from django.urls import path
from .views import ArticleAPIView, ArticleDetails

urlpatterns = [
    # path('article/', article_list),
    path('article/',ArticleAPIView.as_view()),
    path('detail/<int:pk>/', ArticleDetails.as_view()),
]
