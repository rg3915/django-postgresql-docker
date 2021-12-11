from django.db import models


class Article(models.Model):
    title = models.CharField('título', max_length=100)
    subtitle = models.CharField('sub-título', max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'artigo'
        verbose_name_plural = 'artigos'

    def __str__(self):
        return f'{self.title}'
