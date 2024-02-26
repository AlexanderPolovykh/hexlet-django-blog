from django.shortcuts import render, get_object_or_404, redirect

# from django.http import Http404
from django.views import View
from hexlet_django_blog.article.models import Article, ArticleComment

# from .forms import CommentArticleForm
from .forms import ArticleCommentForm, ArticleForm
import logging
from django.contrib import messages


logger = logging.getLogger(__name__)


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


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm(
            {
                "name": "default name default name default name default name default name",
                "body": "default body",
            }
        )
        return render(request, "articles/create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():  # Если данные корректные, то сохраняем данные формы
            form.save()
            messages.success(request, "New Article was checked and saved.")
            return redirect("articles")  # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполн формой
        messages.error(request, "New article is not valid!")
        return render(request, "articles/create.html", {"form": form})


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


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, f"Article '{article.name}' was updated and saved.")
            return redirect('articles')
        messages.error(request, "Article has not been updated!")
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})


class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.success(request, f"Article '{article.name}' was deleted.")
        else:
            messages.error(request, f"Article '{article.name}' was not deleted!")

        return redirect('articles')

# class CommentArticleView(View):

#     def get(self, request, *args, **kwargs):
#         article_by_id = get_object_or_404(ArticleComment, article_id=kwargs["id"])
#         form = CommentArticleForm(
#             initial={"id": kwargs["id"], "content": article_by_id.content}
#         )  # Создаем экземпляр нашей формы
#         return render(
#             request, "articles/comment.html", context={"form": form}  # , "id": kwargs["id"]}
#         )  # Передаем нашу форму в контексте

#     def post(self, request, *args, **kwargs):
#         form = CommentArticleForm(request.POST)  # Получаем данные формы из запроса
#         if form.is_valid():  # Проверяем данные формы на корректность
#             logger.warning('Logger -> Form valid.')
#             article_by_id = Article.objects.get(id=form.cleaned_data["id"])
#             logger.warning('Logger -> id: %d', form.cleaned_data["id"])
#             comment = ArticleComment(
#                 content=form.cleaned_data[
#                     "content"
#                 ],  # Получаем очищенные данные из поля content
#                 # Заполняем оставшиеся поля
#                 article=article_by_id,
#             )
#             comment.save()
#             return render(
#                 request, "articles/comment.html", context={"form": form}  # , "id": kwargs["id"]}
#             )  # Передаем нашу форму в контексте
#         else:
#             raise Http404()


class ArticleCommentView(View):
    def get(self, request, *args, **kwargs):
        article_by_id = get_object_or_404(ArticleComment, article_id=kwargs["id"])
        logger.warning("Logger -> Form valid.")
        form = ArticleCommentForm(initial={"id": kwargs["id"], "content": article_by_id.content})
        return render(
            request, "articles/comment.html", context={"form": form}
        )  # Передаем нашу форму в контексте

    #         )  # Создаем экземпляр нашей формы

    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)  # Получаем данные формы из запроса
        if form.is_valid():  # Проверяем данных формы на корректность
            form.save()

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
