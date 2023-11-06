from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os 

def setup(): 
  options = ChromeOptions()
  options.browser_version = 'latest'
  options.platform_name = 'Windows 11'
  sauce_options = {}
  sauce_options['username'] = os.environ["SAUCE_USERNAME"]
  sauce_options['accessKey'] = os.environ["SAUCE_ACCESS_KEY"]
  sauce_options['build'] = 'duypk5'
  sauce_options['name'] = 'my-test'
  options.set_capability('sauce:options', sauce_options)

  url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"
  driver = webdriver.Remote(command_executor=url, options=options)
  driver.get("https://www.python.org")
  print(driver.title)
  search_bar = driver.find_element(By.NAME, "q")
  search_bar.clear()
  search_bar.send_keys("getting started with python")
  search_bar.send_keys(Keys.RETURN)
  print(driver.current_url)
  driver.close()

if __name__ == '__main__':
  setup()