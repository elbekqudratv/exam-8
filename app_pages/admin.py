from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ('faq_question_uz', 'faq_question_eng', 'faq_answer_uz', 'faq_answer_eng')
    search_fields = ('faq_question_uz', 'faq_question_eng')
    list_filter = ('faq_question_uz', 'faq_question_eng')

    def has_add_permission(self, request):
        return request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff

admin.site.register(FAQ, FAQAdmin)