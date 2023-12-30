from django.contrib import admin
from contact.models import Contact, Category

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'first_last', 'phone')
    ordering = ('-id',)
    search_fields = ('id', 'first_name', 'first_last', 'phone')
    list_per_page = 15
    list_max_show_all = 200

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Ajuste esta linha para ser uma tupla ou lista
    ordering = ('-id',)
