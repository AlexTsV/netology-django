from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    topic = models.CharField(max_length=128, verbose_name='Категория')
    articles_scope = models.ManyToManyField(Article, through='ArticleScope', related_name='scopes')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.topic


class ArticleScope(models.Model):
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, verbose_name='Раздел')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематика статьи'

    def __str__(self):
        return f'{self.article}_{self.scope}'
