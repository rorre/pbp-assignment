from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core import serializers

from mywatchlist.models import MyWatchList


def show_json(request: HttpRequest):
    data = MyWatchList.objects.all()
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json",
    )


def show_xml(request: HttpRequest):
    data = MyWatchList.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data),
        content_type="application/xml",
    )


def show_html(request: HttpRequest):
    data = MyWatchList.objects.all()
    ctx = {"data": data}
    return render(request, "list.html", ctx)
