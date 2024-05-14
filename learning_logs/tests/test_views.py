from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from learning_logs.models import Topic, Entry
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username="testuser", password="123456")
        self.client.login(username="testuser", password="123456")

        self.topic1 = Topic.objects.create(
            text="test text",
            date_added=datetime.now(),
            owner=self.user1
        )

        self.entry1 = Entry.objects.create(
            topic=self.topic1,
            text="another text to try",
            date_added=datetime.now()
        )

    def test_project_index_GET(self):
        response = self.client.get(reverse('learning_logs:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_logs/index.html')

    def test_project_topics_GET(self):
        response = self.client.get(reverse('learning_logs:topics'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_logs/topics.html')

    def test_project_topic_GET(self):
        response = self.client.get(reverse('learning_logs:topic', args=[self.topic1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_logs/topic.html')

    def test_project_new_topic_GET(self):
        response = self.client.get(reverse('learning_logs:new_topic'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_logs/new_topic.html')

    def test_project_new_entry_GET(self):
        response = self.client.get(reverse('learning_logs:new_entry', args=[self.topic1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_logs/new_entry.html')

    def test_project_edit_entry_GET(self):
        response = self.client.get(reverse('learning_logs:edit_entry', args=[self.entry1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_logs/edit_entry.html')

    def test_project_new_topic_POST(self):
        response = self.client.post(reverse('learning_logs:new_topic'), {
            'text': 'New topic'
        })
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertEqual(Topic.objects.last().text, 'New topic')

    def test_project_new_entry_POST(self):
        response = self.client.post(reverse('learning_logs:new_entry', args=[self.topic1.id]), {
            'text': 'New entry'
        })
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertEqual(Entry.objects.last().text, 'New entry')

    def test_project_edit_entry_POST(self):
        response = self.client.post(reverse('learning_logs:edit_entry', args=[self.entry1.id]), {
            'text': 'Updated entry'
        })
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertEqual(Entry.objects.get(id=self.entry1.id).text, 'Updated entry')
