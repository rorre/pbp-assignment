import typing as t
from django.shortcuts import render

from katalog.models import CatalogItem

if t.TYPE_CHECKING:
    from django.http import HttpRequest


def show_catalogs(request: "HttpRequest"):
    items = CatalogItem.objects.all()
    ctx = {
        "items": items,
        "student_name": "Rendy Arya Kemal",
        "student_id": 2106639945,
    }
    return render(request, "katalog.html", ctx)
