import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ct_board.settings")
django.setup()
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from board.models import Boards
from .models import Posts


class PostsAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.board = Boards.objects.create(

        )
        self.post = Posts.objects.create(
            boardID=self.board,
            userID=12345,
            title='Test Post',
            content='This is a test post.',
        )

    def test_search_post_by_postID(self):
        url = reverse('postDetailView') + '?postID=' + str(self.post.postID)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], self.post.content)

    def test_search_posts_by_boardID(self):
        # Test searching the list of posts by boardID
        url = reverse('postDetailView') + f'?boardID={self.board.id}&start=0&size=10'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) <= 10)

    def test_insert_post(self):
        # Test inserting a new post
        url = reverse('your_post_create_url_name')
        data = {
            'boardID': self.board.id,
            'userID': 54321,
            'title': 'New Post',
            'content': 'This is a new post.',
            'anonymous': True,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_post(self):
        # Test updating a post
        url = reverse('your_post_update_url_name') + '?postID=' + str(self.post.postID)
        data = {
            'title': 'Updated Title',
            'content': 'Updated content.',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        # Test deleting a post
        url = reverse('your_post_delete_url_name') + '?postID=' + str(self.post.postID)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_search_followers_by_postID(self):
        # Test searching follower userID list by postID
        # This assumes a mechanism to associate followers with posts exists
        url = reverse('your_followers_list_url_name') + '?postID=' + str(self.post.postID)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assuming the response data is a list of userIDs
        # self.assertIn(12345, response.data)
