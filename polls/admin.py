from django.contrib import admin
from .models import Choice, Question

# 1. Konfiguracja edycji odpowiedzi "wewnątrz" pytania
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Wyświetla 3 dodatkowe puste pola na odpowiedzi

# 2. Główna konfiguracja widoku pytania
class QuestionAdmin(admin.ModelAdmin):
    # Podział pól na sekcje (Fieldsets)
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Informacje o dacie", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    
    # Dodanie odpowiedzi do widoku edycji pytania
    inlines = [ChoiceInline]
    
    # Co ma być widać na liście wszystkich pytań
    list_display = ["question_text", "pub_date", "was_published_recently"]
    
    # Panel filtrów po prawej stronie
    list_filter = ["pub_date"]
    
    # Wyszukiwarka na górze
    search_fields = ["question_text"]

# 3. Rejestracja modeli
admin.site.register(Question, QuestionAdmin)

# 4. Personalizacja całego panelu Admina (napisy na górze)
admin.site.site_header = "System Ankietowy - Panel Sterowania"
admin.site.site_title = "Portal Ankiet"
admin.site.index_title = "Witaj w zarządzaniu ankietami"