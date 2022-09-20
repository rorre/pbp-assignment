from django.urls import path

from mywatchlist.views import show_html, show_json, show_xml

app_name = "mywatchlist"

urlpatterns = [
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("html/", show_html, name="show_html"),
]
