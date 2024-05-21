from django.test import TestCase
from learning_logs.forms import TopicForm


class TestTopicForm(TestCase):
    def test_form_valid_data(self):
        form = TopicForm(data={'text': 'Test Topic'})
        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        form = TopicForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_form_empty_string(self):
        form = TopicForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], ["This field is required."])

    def test_form_long_string(self):
        form = TopicForm(data={'text': 'a' * 210})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], ["Ensure this value has at most 200 characters (it has 210)."])