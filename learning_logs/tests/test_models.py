from django.contrib.auth.models import User
from django.test import TestCase
from learning_logs.models import Topic, Entry
from datetime import datetime


class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser', password='12345')
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

    def test_topic_creation(self):
        self.assertEqual(self.topic1.text, 'test text')
        self.assertEqual(self.topic1.owner, self.user1)

    def test_entry_creation(self):
        self.assertEqual(self.entry1.text, 'another text to try')
        self.assertEqual(self.entry1.topic, self.topic1)

    # def test_quantitat_de_lletres_diferents(self):
    #     self.assertEqual(self.topic1.quantitat_de_lletres_diferents(), len(set('test text')))
