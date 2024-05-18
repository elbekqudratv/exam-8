from django.db import models

# Create your models here.

class PublicationType(models.Model):
    type_name = models.CharField(max_length=255)
    type_desc = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.type_name
    
    class Meta:
        db_table = 'pubtypes'
        verbose_name = 'Pubtypes'
        verbose_name_plural = 'pubtype'


class Gender(models.Model):
    gender_name = models.CharField(max_length=255)

    def __str__(self):
        return self.gender_name
    
    class Meta:
        db_table = 'genders'
        verbose_name = 'Gender'
        verbose_name_plural = 'gender'


class Publications(models.Model):
    pub_name_uz = models.CharField(max_length=255)
    pub_name_eng = models.CharField(max_length=255, null=True)
    pub_text_uz = models.TextField()
    pub_text_eng = models.CharField(max_length=255, null=True)
    pub_date = models.DateField()
    pub_tegs = models.CharField(max_length=255)
    pub_img = models.BinaryField()
    pub_author = models.ForeignKey('Author', on_delete=models.CASCADE)
    pub_desc_uz = models.CharField(max_length=255)
    pub_desc_eng = models.CharField(max_length=255, null=True)
    pub_code = models.IntegerField()
    pub_file = models.BinaryField()
    pub_type = models.ForeignKey(PublicationType, on_delete=models.CASCADE)

    def __str__(self):
        return self.pub_name_uz
    
    class Meta:
        db_table = 'publications'
        verbose_name = 'Publication'
        verbose_name_plural = 'publication'


class Author(models.Model):
    author_name = models.CharField(max_length=255)
    author_lastname = models.CharField(max_length=255)
    author_age = models.IntegerField()
    author_country = models.CharField(max_length=255)
    author_gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author_name} {self.author_lastname}"
    
    class Meta:
        db_table = 'authors'
        verbose_name = 'Author'
        verbose_name_plural = 'author'