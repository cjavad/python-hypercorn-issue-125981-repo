from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Set up Chrome options
chrome_options = ChromeOptions()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors

driver = webdriver.Chrome(options=chrome_options)