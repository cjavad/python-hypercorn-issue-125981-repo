import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class TestServerRequests(unittest.TestCase):
    def setUp(self):
        """Initialize both Chrome and Firefox drivers with SSL-ignore settings."""
        
        # Set up Chrome options
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors
        
        # Set up Firefox options and profile
        firefox_options = FirefoxOptions()
        firefox_options.headless = True  # Run Firefox in headless mode
        firefox_options.accept_insecure_certs= True

        # Initialize drivers
        self.chrome_driver = webdriver.Chrome(options=chrome_options)
        self.firefox_driver = webdriver.Firefox(options=firefox_options)

        # Define the target URL
        self.url = "https://localhost:3000"

    def test_chrome_request(self):
        """Test if Chrome can access the server and receive the expected response."""
        self.chrome_driver.get(self.url)
        
        # Check if the page contains expected content (e.g., "Hello world!")
        self.assertIn("Hello world!", self.chrome_driver.page_source)

    def test_firefox_request(self):
        """Test if Firefox can access the server and receive the expected response."""
        self.firefox_driver.get(self.url)
        
        # Check if the page contains expected content (e.g., "Hello world!")
        self.assertIn("Hello world!", self.firefox_driver.page_source)

    def tearDown(self):
        """Close all browser instances."""
        self.chrome_driver.quit()
        self.firefox_driver.quit()

if __name__ == "__main__":
    # Run the test suite
    unittest.main()
