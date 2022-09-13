import typing as t
from django.shortcuts import render

from katalog.models import CatalogItem

if t.TYPE_CHECKING:
    from django.http import HttpRequest


def show_catalogs(request: "HttpRequest"):
    items = CatalogItem.objects.all()
    ctx = {
        "items": items,
        # TODO: Fake data xd
        "student_name": "Ren",
        "student_id": 2,
    }
    return render(request, "katalog.html", ctx)
