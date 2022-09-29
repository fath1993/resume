from django.db import models


class KeyWord(models.Model):
    keyword = models.CharField(max_length=255, null=False, blank=False, verbose_name='keyword')

    def __str__(self):
        return str(self.keyword)[:100]

    class Meta:
        verbose_name = 'keyword'
        verbose_name_plural = 'keywords'


class WebsiteSpecification(models.Model):
    meta_keywords = models.ManyToManyField(KeyWord, blank=True, verbose_name='meta keywords')
    meta_description = models.CharField(max_length=255, null=False, blank=False, verbose_name='meta description')
    meta_author = models.CharField(max_length=255, null=False, blank=False, verbose_name='meta author')
    meta_title = models.CharField(max_length=255, null=False, blank=False, verbose_name='meta title')

    def __str__(self):
        return str(self.meta_title)[:100]

    class Meta:
        verbose_name = 'website specification'
        verbose_name_plural = 'website specifications'
