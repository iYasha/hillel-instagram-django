from django.contrib import admin
from cards.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'user', 'updated_at', 'created_at')
    list_filter = ('id', 'description', 'user')
    search_fields = ('id', 'description', 'updated_at', 'created_at')
    list_per_page = 25
    ordering = ['-created_at']


