from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hello"),
    path("facts/", views.facts_json, name="facts_json"),
    path("random/", views.random_fact_page, name="random_fact_page"),
    path("random.json", views.random_fact_json, name="random_fact_json"),
    path("chart/", views.facts_chart, name="facts_chart"),
]
