from django.shortcuts import render, get_object_or_404
from django.views import View
from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )

    # context = {"app_name": "Article Application"}
    # def get(self, request):
    # return render(request, template_name="articles/index.html", context=self.context)


# def index(request, tags="", article_id=0):
#     return render(
#         request,
#         "articles/index.html",
#         context={
#             "tags": tags,
#             "article_id": article_id,
#         },
#     )
