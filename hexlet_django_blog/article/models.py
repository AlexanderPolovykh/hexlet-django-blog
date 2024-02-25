from django.db import models


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=20)  # название статьи
    body = models.TextField()  # тело статьи
    timestamp = models.DateTimeField(auto_now_add=True)


class ArticleComment(models.Model):
    content = models.CharField("content", max_length=100)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"name: '{self.name}', body: '{self.body}'"
