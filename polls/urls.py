from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # /polls/
    path("", views.IndexView.as_view(), name="index"),
    
    # /polls/5/
    # DetailView oczekuje parametru o nazwie 'pk'
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    
    # /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    
    # /polls/5/vote/
    # Tutaj zostajemy przy question_id, bo obsługuje to zwykła funkcja w views.py
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
from django.contrib import admin

admin.site.site_header = "System Ankiet Tutorial"
admin.site.site_title = "Portal Admina"
admin.site.index_title = "Zarządzanie ankietami"