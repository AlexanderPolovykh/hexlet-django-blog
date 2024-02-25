from django.urls import path
from hexlet_django_blog.article.views import (
    IndexView,
    ArticleView,
    ArticleCommentView,
    ArticleFormCreateView,
)  # CommentArticleView

urlpatterns = [
    # path('', views.index, name="article"),
    # path('<str:tags>/', views.index, name="article"),
    # path('<str:tags>/<int:article_id>/', views.index, name="article"),
    path("", IndexView.as_view(), name="articles"),
    path("<int:id>/", ArticleView.as_view(), name="article_id"),
    # path("<int:id>/comment", CommentArticleView.as_view(), name="comment_create"),
    path("create/", ArticleFormCreateView.as_view(), name="articles_create"),
    path("<int:id>/comment", ArticleCommentView.as_view(), name="comment_create"),
]
