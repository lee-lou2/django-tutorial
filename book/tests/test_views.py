import logging

from rest_framework.test import APITestCase

from book.models.book import Book


class TestBook(APITestCase):
    def setUp(self) -> None:
        logging.basicConfig(level="INFO")

    def test_도서_생성(self):
        resp = self.client.post("/v1/book/", data={"title": "test"}, json=True)
        self.assertEqual(resp.status_code, 201)

    def test_도서_조회(self):
        obj = Book.objects.create(title="test")
        resp = self.client.get(f"/v1/book/{obj.pk}/")
        self.assertEqual(resp.status_code, 200)
