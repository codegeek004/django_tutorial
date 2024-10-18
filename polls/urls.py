from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index"),
        path("<int:question_id>/", views.detail, name="detail"),
        path("<int:question_id>/results", views.results, name="results"),
        path("<int:question_id>/vote", views.vote, name="vote"),
        # you can use the last argument as reference to the url in templates or views instead of hardcoding the url
        ]


