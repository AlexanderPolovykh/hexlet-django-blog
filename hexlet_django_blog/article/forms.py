# from django import forms  # Импортируем формы Django
from django.forms import ModelForm
from .models import ArticleComment, Article

# class CommentArticleForm(forms.Form):
#     id = forms.IntegerField(label='ID Статьи')  # , initial=1)
#     content = forms.CharField(label="Комментарий")  # Текст комментария


class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ["content", "article"]


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
