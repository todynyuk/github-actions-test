import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.DEBUG)

capabilities = {
    "browserName": "firefox",
    "version": "88.0",
    "platform": "LINUX"
}

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=capabilities
)

try:
    logging.info('Session ID is: %s' % driver.session_id)
    #print('Session ID is: %s' % driver.session_id)
    logging.info('Opening the page...')
    #print('Opening the page...')
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    logging.info('Taking screenshot...')
    #print('Taking screenshot...')
    driver.get_screenshot_as_file(driver.session_id + '.png')
finally:
    driver.quit()
