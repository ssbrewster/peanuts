from django.core.urlresolvers import reversed
from rest_framework import status
from rest_framework.test import APITestCase


class AuthorTests(APITestCase):
    def test_create_author(self):
        """
        Test that the post method to create a new author is successful,
        returns an HTTP_201_CREATED and the data in the response is equal to
        the data in the post method
        """
        url = reverse("author-detail")
        data = {"username": "Mr Bloggy"}
        response = self.client.post(url, data, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)}
