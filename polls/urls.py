from django.urls import path
from . import views

urlpatterns = [
        path("", views.IndexView.as_view(), name="index"),
        path("<int:pk>/", views.DetailView.as_view(), name="detail"),
        path("<int:pk>/results", views.ResultsView.as_view(), name="results"),
        path("<int:question_id>/vote", views.vote, name="vote"),
        # you can use the last argument as reference to the url in templates or views instead of hardcoding the url
        ]


