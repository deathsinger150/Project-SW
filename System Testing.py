from selenium import webdriver
import unittest

class TestSystemWorkflow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_admin_workflow(self):
        driver = self.driver
        driver.get("http://localhost:8000/login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin123")
        driver.find_element_by_name("login").click()

        # Verify dashboard loads
        self.assertIn("Admin Dashboard", driver.page_source)

        # Create a club
        driver.find_element_by_name("create_club").click()
        driver.find_element_by_name("club_name").send_keys("Tech Club")
        driver.find_element_by_name("submit").click()

        # Verify club creation
        self.assertIn("Tech Club", driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
