from django.test import SimpleTestCase
from learning_logs.forms import TopicForm, EntryForm


class TestForms(SimpleTestCase):
    def test_topic_form_valid_data(self):
        form = TopicForm(data={
            'text': 'Test Topic'
        })

        self.assertTrue(form.is_valid())

    def test_topic_form_no_data(self):
        form = TopicForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_entry_form_valid_data(self):
        form = EntryForm(data={
            'text': 'Test Entry'
        })

        self.assertTrue(form.is_valid())

    def test_entry_form_no_data(self):
        form = EntryForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
