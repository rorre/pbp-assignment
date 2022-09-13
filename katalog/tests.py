from django.urls import reverse
from django.test import TestCase
from katalog.models import CatalogItem


class AnimalTestCase(TestCase):
    SAMPLE_CASES = [
        {
            "item_name": "Sample 1",
            "item_price": 1000,
            "item_stock": 1,
            "description": "Is an example",
            "rating": 5,
            "item_url": "https://google.com",
        },
        {
            "item_name": "Very cool very swag",
            "item_price": 69420,
            "item_stock": 100,
            "description": "Swagging",
            "rating": 9,
            "item_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        },
        {
            "item_name": "Nice item",
            "item_price": 5000,
            "item_stock": 200,
            "description": "Very nice item",
            "rating": 8,
            "item_url": "https://www.youtube.com/watch?v=gDjMZvYWUdo",
        },
    ]

    def setUp(self):
        for case in self.SAMPLE_CASES:
            CatalogItem.objects.create(**case)

    def test_fetch(self):
        response = self.client.get(reverse("katalog:show_catalogs"))
        self.assertContains(response, "Sample 1")  # Name from sample 1
        self.assertContains(response, "69420")  # Price from sample 2
        self.assertContains(response, "200")  # Stok from sample 3
        self.assertContains(response, "Swagging")  # Desc from sample 2
        self.assertContains(response, "8")  # Rating from sample 3
        self.assertContains(response, "google")  # URL from sasmple 1
