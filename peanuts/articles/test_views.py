from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ArticlesTests(APITestCase):
    def test_create_article(self):
        """
        Test that the post method to create an article is successful, returns an HTTP_201_CREATED status code
        and the data in the response is equal to the data in the post method
        """
        url = reverse("article-detail")
        data = {"author": "Simon Brewster", "title": "Test article title", "body": "This is an amazing article. It's"
                                                                                   "so great writing a blog."}
        response = self.client.post(url, data, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)


    def test_list_articles(self):
        """
        Test that the get method to list all articles is successful and returns
        an HTTP_201_CREATED status_code
        """
        url = reverse("article-list")
        response = self.client.get(url, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
