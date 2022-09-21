from django.test import TestCase
from django.urls import reverse

from mywatchlist.models import MyWatchList


class MyWatchListTest(TestCase):

    SAMPLE = {
        "watched": True,
        "title": "Everything Everywhere All At Once",
        "rating": 4,
        "release_date": "2022-06-22",
        "review": "Very epic",
    }

    def setUp(self) -> None:
        MyWatchList.objects.create(**self.SAMPLE)

    def test_200(self):
        response = self.client.get(reverse("mywatchlist:show_json"))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse("mywatchlist:show_xml"))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse("mywatchlist:show_xml"))
        self.assertEqual(response.status_code, 200)
