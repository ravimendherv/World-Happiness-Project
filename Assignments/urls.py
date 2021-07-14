from django.urls import path
from .views import getDetailsByCountryName, getDetailsByLadderScore
urlpatterns = [
    path("v1/country/<country_name>/",getDetailsByCountryName),
    path("v1/score-range/",getDetailsByLadderScore),
]