from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Set up Firefox options and profile
firefox_options = FirefoxOptions()
firefox_options.headless = True  # Run Firefox in headless mode
firefox_options.accept_insecure_certs= True

driver = webdriver.Firefox(options=firefox_options)