from django.contrib import admin
from .models import Question, Option, PersonalityResult


class OptionInline(admin.TabularInline):
    model = Option
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "order")
    ordering = ("order",)
    inlines = [OptionInline]


@admin.register(PersonalityResult)
class PersonalityResultAdmin(admin.ModelAdmin):
    list_display = ("user", "learning_level", "total_score", "created_at")
