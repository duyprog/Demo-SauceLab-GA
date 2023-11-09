import os
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

caps = {}
caps['platformName'] = 'iOS'
caps['appium:deviceName'] = 'iPhone 12'
caps['appium:platformVersion'] = '16'
caps['appium:automationName'] = 'XCUITest'
caps['sauce:options'] = {}
caps['sauce:options']['username'] = os.environ["SAUCE_USERNAME"]
caps['sauce:options']['accessKey'] = os.environ["SAUCE_ACCESS_KEY"]
caps['sauce:options']['build'] = 'test'
caps['sauce:options']['name'] = 'ios-test'
caps['app'] = "https://testingbot.com/appium/sample.ipa"

url = 'https://ondemand.us-west-1.saucelabs.com:443/wd/hub'
driver = webdriver.Remote(url, caps)

inputA = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputA"))
)
inputA.send_keys("10")

inputB = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputB"))
)
inputB.send_keys("5")

driver.quit()