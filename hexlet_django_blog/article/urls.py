from django.urls import path

from hexlet_django_blog.article.views import IndexView, ArticleView

urlpatterns = [
    # path('', views.index, name="article"),
    # path('<str:tags>/', views.index, name="article"),
    # path('<str:tags>/<int:article_id>/', views.index, name="article"),
    path("", IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view(), name='article_id'),
]
