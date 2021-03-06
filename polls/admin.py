from django.contrib import admin

# Register your models here.

from .models import *


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    search_fields = ['question_text']

    list_filter = ['pub_date']

    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)

admin.site.register(Person)

admin.site.register(Group)

admin.site.register(Membership)

admin.site.register(Message)
