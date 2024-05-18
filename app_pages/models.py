from django.db import models

# Create your models here.
class Requirements(models.Model):
    requirement_name_uz = models.CharField(max_length=255)
    requirement_name_eng = models.CharField(max_length=255, null=True)
    requirement_text_uz = models.TextField()
    requirement_text_eng = models.TextField(null=True)

    def __str__(self):
        return self.requirement_name_uz
    
    class Meta:
        db_table = 'requirements'
        verbose_name = 'Requirement'
        verbose_name_plural = 'requirement'


class FAQ(models.Model):
    faq_question_uz = models.CharField(max_length=255)
    faq_question_eng = models.CharField(max_length=255, null=True)
    faq_answer_uz = models.TextField()
    faq_answer_eng = models.TextField(null=True)

    def __str__(self):
        return self.faq_question_uz
    
    class Meta:
        db_table = 'faqs'
        verbose_name = 'FAQ'
        verbose_name_plural = 'faq'


class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_sender = models.EmailField()
    contact_message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name
    
    class Meta:
        db_table = 'contacs'
        verbose_name = 'Contact'
        verbose_name_plural = 'contact'