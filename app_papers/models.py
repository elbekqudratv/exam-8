from django.db import models
from django.contrib.auth.models import User
from app_publications.models import Author

class Paper(models.Model):
    paper_name_uz = models.CharField(max_length=255)
    paper_name_eng = models.CharField(max_length=255, null=True)
    paper_desc_uz = models.CharField(max_length=255)
    paper_desc_eng = models.CharField(max_length=255, null=True)
    paper_text_uz = models.TextField()
    paper_text_eng = models.TextField(null=True)
    paper_date = models.DateField()
    paper_author = models.ForeignKey(User, on_delete=models.CASCADE)
    paper_view_count = models.IntegerField(default=0)
    paper_code = models.IntegerField(unique=True)
    paper_file = models.FileField(upload_to='papers/')

    def __str__(self):
        return self.paper_name_uz

    class Meta:
        db_table = 'papers'
        verbose_name = 'Paper'
        verbose_name_plural = 'Papers'


class Article(models.Model):
    article_text_uz = models.TextField()
    article_text_eng = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    publication = models.ForeignKey('Publication', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.article_text_uz

    def delete(self, *args, **kwargs):
        self.publication = None  # Delete the reference to publication before deleting the article
        self.save()
        super().delete(*args, **kwargs)

    class Meta:
        db_table = 'articles'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Annotation(models.Model):
    anno_text_uz = models.TextField()
    anno_text_eng = models.TextField(null=True)
    anno_date = models.DateField()
    anno_author = models.ForeignKey(User, on_delete=models.CASCADE)
    anno_view_count = models.IntegerField(default=0)
    anno_keyword = models.CharField(max_length=255)
    anno_file = models.FileField(upload_to='annotations/')

    def __str__(self):
        return self.anno_text_uz

    class Meta:
        db_table = 'annotations'
        verbose_name = 'Annotation'
        verbose_name_plural = 'Annotations'


class Reference(models.Model):
    reference_name_uz = models.CharField(max_length=255)
    reference_name_eng = models.CharField(max_length=255, null=True)
    reference_text_uz = models.TextField()
    reference_text_eng = models.TextField(null=True)
    reference_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.reference_name_uz

    class Meta:
        db_table = 'references'
        verbose_name = 'Reference'
        verbose_name_plural = 'References'


class Publication(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_articles(self):
        return Article.objects.filter(publication=self)

    class Meta:
        db_table = 'publications'
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
