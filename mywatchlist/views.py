from django.core import serializers
from django.db.models import QuerySet
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

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
    data: QuerySet[MyWatchList] = MyWatchList.objects.all()

    total = data.count()
    watched_count = 0
    for watch_data in data:
        if watch_data.watched:
            watched_count += 1

    has_more_watch = watched_count >= (total - watched_count)
    ctx = {
        "data": data,
        "has_more_watch": has_more_watch,
    }
    return render(request, "list.html", ctx)
