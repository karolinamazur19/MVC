from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """Pozwala na edycję odpowiedzi bezpośrednio w widoku pytania."""
    model = Choice
    extra = 3  # Domyślnie wyświetla 3 puste pola na nowe odpowiedzi


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Konfiguracja panelu administracyjnego dla pytań."""
    
    # Podział pól na sekcje (Fieldsets)
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    
    # Dodanie odpowiedzi jako elementu osadzonego
    inlines = [ChoiceInline]

    # Kolumny wyświetlane na liście wszystkich pytań
    list_display = ["question_text", "pub_date", "was_published_recently"]
    
    # Dodanie bocznego panelu filtrowania po dacie
    list_filter = ["pub_date"]
    
    # Dodanie wyszukiwarki tekstowej
    search_fields = ["question_text"]

# Opcjonalnie: Rejestracja Choice osobno (zazwyczaj niepotrzebne przy użyciu Inlines)
# admin.site.register(Choice)