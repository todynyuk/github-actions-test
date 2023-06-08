import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

 def test_firefox():
    capabilities = {
        "browserName": "firefox",
        "version": "88.0",
        "platform": "LINUX"
    }
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=capabilities
    )
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
    word = "AGM A9"
    count = 0
    try:
        logging.info('Session ID is: %s' % driver.session_id)
        logging.info('Opening the page...')
        driver.get("https://rozetka.com.ua/ua/")
        assert "ROZETKA" in driver.title, "Title not contains ROZETKA"
        search_input = driver.find_element(By.XPATH, "//input[contains(@class, 'search-form')]")
        search_input.click()
        search_input.clear()
        search_input.send_keys(word)
        search_input.submit()
        search_button = driver.find_element(By.XPATH, "//button[contains(@class, 'button_color_green')]")
        search_button.click()
        search_results = WebDriverWait(driver, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "goods-tile__title")))
        print("Length search_results: ", len(search_results))
        assert len(search_results) > 0, "Length == 0"
        logging.info("Verify is the result contain '%s'", str(word))
        for result in search_results:
            count += 1
            if count > 5:
                break
            title_text = result.text.lower()
            logging.info("Checking the following: '%s'", title_text)
            assert word.lower() in title_text, "Search text not contains in good's title text"
    except AssertionError:
        driver.get_screenshot_as_file(driver.session_id + '.png')
        raise
    finally:
        driver.quit()
