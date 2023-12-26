from django.contrib import admin
from contact.models import Contact  # Importa o modelo Contact diretamente

@admin.register(Contact)  # Usa Contact diretamente, sem precisar do prefixo "models."
class ContactAdmin(admin.ModelAdmin):
    # Seu código para a administração do modelo Contact
    list_display = 'first_name', 'first_last', 'phone'
    ordering = '-id',
    
    search_fields = 'id' ,'first_name', 'first_last', 'phone',
    list_per_page = 15
    list_max_show_all = 200
