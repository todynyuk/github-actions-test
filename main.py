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

word = "AGM A9"
count = 0
try:
    logging.info('Session ID is: %s' % driver.session_id)
    logging.info('Opening the page...')
    driver.get("https://rozetka.com.ua/ua/")
    assert "ROZETKA" in driver.title
    search_input = driver.find_element(By.NAME, "search")
    search_input.clear()
    search_input.send_keys(word)
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class*='button_color_green']")
    search_button.click()
    search_results = driver.find_elements(By.CLASS_NAME, "goods-tile__title").text
    assert len(search_results) > 0
    logging.info("Verify is the result contain '%s'", str(word))
    for result in search_results:
        count += 1
        if count > 5:
            break
        title_text = result.lower()
        logging.info("Checking the following: '%s'", title_text)
        assert word.lower() in title_text
except AssertionError:
    driver.get_screenshot_as_file(driver.session_id + '.png')
    raise
finally:
    driver.quit()
        
