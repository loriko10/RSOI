'''
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import LiveServerTestCase
from django.core.urlresolvers import reverse
from selenium.common.exceptions import NoSuchElementException
import os
import sys
import time
fdshjid
from selenium import webdriver


class AdminTestCase(LiveServerTestCase):
    def setUp(self):
        # setUp is where you instantiate the selenium webdriver and loads the browser.
        User.objects.create_superuser(username='admin', password='1qazxsw2', email='admin@example.com')

        self.webdriver = webdriver.Chrome()
        self.webdriver.implicitly_wait(100)
        self.live_server_url = "http://localhost:8000"
        super(AdminTestCase, self).setUp()

    def tearDown(self):
        # Call tearDown to close the web browser
        self.webdriver.quit()
        super(AdminTestCase, self).tearDown()

    def test_01_create_user(self):
        """
        Django admin create user test
        This test will create a user in django admin and assert that
        page is redirected to the new user change form.
        """
        self.webdriver.get('%s%s' % (self.live_server_url, "/admin/"))
        # Fill login information of admin
        username = self.webdriver.find_element_by_id("id_username")
        username.send_keys("admin")
        password = self.webdriver.find_element_by_id("id_password")
        password.send_keys("1qazxsw2")

        # Locate Login button and click it
        time.sleep(2)
        self.webdriver.find_element_by_xpath('//input[@value="Log in"]').click()
        self.webdriver.get('%s%s' % (self.live_server_url, "/admin/auth/user/add/"))

        # Fill the create user form with username and password
        self.webdriver.find_element_by_id("id_username").send_keys("test_user")
        self.webdriver.find_element_by_id("id_password1").send_keys("1qazxsw2")
        self.webdriver.find_element_by_id("id_password2").send_keys("1qazxsw2")

        # Forms can be submitted directly by calling its method submit
        time.sleep(2)
        self.webdriver.find_element_by_xpath('//input[@value="Save"]').click()
        self.assertIn("Change user", self.webdriver.title)
        self.tearDown()

    def test_02_add_task(self):
        self.webdriver.get('%s%s' % (self.live_server_url, "/login/"))
        self.webdriver.find_element_by_id("id_username").send_keys("admin")
        self.webdriver.find_element_by_id("id_password").send_keys("1qazxsw2")
        self.webdriver.find_element_by_id("id_submit").click()
        time.sleep(2)
        self.webdriver.find_element_by_id("addTask").click()
        self.webdriver.find_element_by_id("taskName").send_keys("test_task_name")
        time.sleep(2)
        self.webdriver.find_element_by_id("focusedInput").send_keys("test_long_description")
        time.sleep(2)
        element = self.webdriver.find_element_by_xpath("//select[@id='students']")
        element.find_element_by_xpath('//option[@data-tokens="test_user"]').click()
        self.webdriver.find_element_by_id("saveButton").click()
        time.sleep(2)
        self.tearDown()

    def test_03_change_task_status(self):
        self.webdriver.get('%s%s' % (self.live_server_url, "/login/"))
        self.webdriver.find_element_by_id("id_username").send_keys("test_user")
        self.webdriver.find_element_by_id("id_password").send_keys("1qazxsw2")
        self.webdriver.find_element_by_id("id_submit").click()
        element = self.webdriver.find_element_by_link_text("Edit")
        element.click()
        element.find_element_by_xpath("//a[@status=3]").click()
        #element.find_element_by_tag_name("option").click()
        #self.webdriver.find_element_by_id("saveButton").click()
        time.sleep(2)
        self.tearDown()


    def test_04_delete_task(self):
        self.webdriver.get('%s%s' % (self.live_server_url,  "/admin/"))

        # Fill login information of admin
        username = self.webdriver.find_element_by_id("id_username")
        username.send_keys("admin")
        password = self.webdriver.find_element_by_id("id_password")
        password.send_keys("1qazxsw2")

        # Locate Login button and click it
        time.sleep(2)
        self.webdriver.find_element_by_xpath('//input[@value="Log in"]').click()
        self.webdriver.get('%s%s' % (self.live_server_url, "/admin/base/task/"))

        # Fill the create user form with username and password
        self.webdriver.find_element_by_link_text("Task object").click()
        time.sleep(2)
        self.assertIn("Change task ", self.webdriver.title)
        time.sleep(2)
        self.webdriver.find_element_by_link_text("Delete").click()
        time.sleep(2)
        self.webdriver.find_element_by_xpath('//input[@value="Yes, I\'m sure"]').click()
        #print(self.webdriver.title)
        self.assertIn("Select task to change", self.webdriver.title)
        self.tearDown()

    def test_05_check_task_status(self):
        self.webdriver.get('%s%s' % (self.live_server_url, "/login/"))
        self.webdriver.find_element_by_id("id_username").send_keys("test_user")
        self.webdriver.find_element_by_id("id_password").send_keys("1qazxsw2")
        self.webdriver.find_element_by_id("id_submit").click()
        self.assertTrue(self.webdriver.title)
#        try:
#            self.webdriver.find_element_by_link_text("Edit")
#            self.assertFalse(True)
#        except NoSuchElementException:
#            self.assertFalse(False)
        time.sleep(2)
        self.tearDown()

    def test_06_delete_user(self):
        """
        Django admin create user test
        This test will create a user in django admin and assert that
        page is redirected to the new user change form.
        """
        self.webdriver.get('%s%s' % (self.live_server_url,  "/admin/"))

        # Fill login information of admin
        username = self.webdriver.find_element_by_id("id_username")
        username.send_keys("admin")
        password = self.webdriver.find_element_by_id("id_password")
        password.send_keys("1qazxsw2")

        # Locate Login button and click it
        time.sleep(2)
        self.webdriver.find_element_by_xpath('//input[@value="Log in"]').click()
        self.webdriver.get('%s%s' % (self.live_server_url, "/admin/auth/user/"))

        self.webdriver.find_element_by_link_text("test_user").click()
        time.sleep(2)
        self.assertIn("Change user ", self.webdriver.title)
        time.sleep(2)
        self.webdriver.find_element_by_link_text("Delete").click()
        time.sleep(2)
        self.webdriver.find_element_by_xpath('//input[@value="Yes, I\'m sure"]').click()
        self.assertIn("Select user to change", self.webdriver.title)
        self.tearDown()
'''
