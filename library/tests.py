# from django.test import TestCase
# from rest_framework.test import APIClient, APITestCase
# from .models import Author
# from rest_framework import status
#
#
# class AuthorViewsetTest(TestCase):
#     def setUp(self):
#         self.author1 = Author.objects.create(author_name='Uriel Sepa')
#         self.author2 = Author.objects.create(author_name='Magnus Tief')
#
#     def create_author_test(self):
#         client = APIClient()
#         data = {'author_name': 'Tina Tury'}
#         response = client.post('/api/author/', data)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(Author.objects.count(), 3)
#
#     def list_author_test(self):
#         client = APIClient()
#         response = client.get('api/author')
#         self.assertEqual(response.status_code, 200)
#
#
