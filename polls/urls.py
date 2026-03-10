from django.urls import path
from . import views

app_name = "polls"  # TEJ LINII CI BRAKUJE!

urlpatterns = [
    # np: /polls/
    path("", views.index, name="index"),
    # np: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # np: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # np: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]