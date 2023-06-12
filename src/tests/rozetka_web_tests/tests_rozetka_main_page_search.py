import pytest
from selenium.webdriver.common.by import By
from loguru import logger
import time,os

class TestsRozetkaMainPageSearch:

    @pytest.mark.label("Search", "correct")
    def test_correct_search(self, driver):
        search_text = "Agm A9"
        logger.remove(0)
        logger.add(sys.stdout, level="TRACE") 
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        main_page.open()
        time.sleep(2)
        logger.info("Rozetka main page is opened")
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, "input[name='search']").send_keys(search_text)
        driver.find_element(By.CSS_SELECTOR, "button[class*='button_color_green']").click()
        button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='goods-tile__title']"))).text
        assert search_text.lower() in str(button).lower(), "Search text not contains in all goods title texts"
        logger.info('Test was successful')
        time.sleep(5)
        if os.path.exists(os.path.join(os.getcwd(), 'output')):
            shutil.rmtree(os.path.join(os.getcwd(), 'output'))
        os.mkdir('output')
        driver.save_screenshot('output/screen.png')
        driver.close()
