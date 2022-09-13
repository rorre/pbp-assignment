from django.urls import path
from katalog.views import show_catalogs

app_name = "katalog"

urlpatterns = [
    path("", show_catalogs, name="show_catalogs"),
]
