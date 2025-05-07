from django.contrib import admin
from .models import Poll, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'active')
    list_filter = ['pub_date', 'active']
    search_fields = ['question']
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
