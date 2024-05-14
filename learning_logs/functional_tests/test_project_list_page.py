from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from learning_logs.models import Topic, Entry


class TestProjectListPage(StaticLiveServerTestCase):
    def setUp(self):
        options = Options()
        options.binary_location = 'functional_tests/chromedriver'
        self.browser = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.browser, 10)

    def tearDown(self):
        self.browser.quit()

    def test_create_new_topic(self):
        self.browser.get(self.live_server_url + reverse('learning_logs:new_topic'))
        inputbox = self.wait.until(EC.presence_of_element_located((By.ID, 'id_text')))
        inputbox.send_keys('New Topic')
        inputbox.submit()
        self.wait.until(EC.text_to_be_present_in_element((By.ID, 'id_topic_list'), 'New Topic'))

    def test_view_topic_details(self):
        Topic.objects.create(text='New Topic')
        self.browser.get(self.live_server_url + reverse('learning_logs:topics'))
        link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'New Topic')))
        link.click()
        header_text = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1'))).text
        self.assertIn('New Topic', header_text)

    def test_edit_topic(self):
        topic = Topic.objects.create(text='New Topic')
        self.browser.get(self.live_server_url + reverse('learning_logs:edit_topic', args=[topic.id]))
        inputbox = self.wait.until(EC.presence_of_element_located((By.ID, 'id_text')))
        inputbox.clear()
        inputbox.send_keys('Updated Topic')
        inputbox.submit()
        self.wait.until(EC.text_to_be_present_in_element((By.ID, 'id_topic_list'), 'Updated Topic'))

    def test_delete_topic(self):
        topic = Topic.objects.create(text='New Topic')
        self.browser.get(self.live_server_url + reverse('learning_logs:delete_topic', args=[topic.id]))
        confirm_button = self.wait.until(EC.presence_of_element_located((By.ID, 'id_confirm_delete')))
        confirm_button.click()
        self.wait.until(EC.invisibility_of_element_located((By.LINK_TEXT, 'New Topic')))
