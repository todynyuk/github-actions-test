import time
from pages.device_page import DevicePage
from pages.devices_category_page import DeviceCategory
from pages.main_page import MainPage
from pages.sub_category_page import SubCategory
#import logging
from loguru import logger
import pyautogui
import time,os

class TestDetailsPage:
    def testItemRamAndPrice(self, driver):
        myScreenshot = pyautogui.screenshot()
        logger.remove(0)
        logger.add(sys.stdout, level="TRACE") 
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        main_page.open()
        myScreenshot.save(r'Path to save screenshot\file name.png')
        logger.info("Rozetka main page is opened")
        main_page.click_universal_category_link(driver, "Смартфони")
        logger.info("Page Smartphones is opened")
        SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
        logger.info("Page Mobile is opened")
        DeviceCategory.choose_ram_сapacity(self, driver, 12)
        DeviceCategory.click_check_box_filter(self, driver, "Синій")
        smartphone_price = DeviceCategory.getSmartphonePriceText(self, driver, 1)
        DeviceCategory.clickLinkMoreAboutDevice(self, driver, 1)
        logger.info("Page MoreAboutDevice is opened")
        short_characteristics = DevicePage.verify_device_short_characteristic(self, driver, 12)
        chosen_device_price = DevicePage.get_chosen_product_price(self, driver)
        assert short_characteristics, "Short_characteristics don't contains chosen ram capacity"
        assert str(smartphone_price) == chosen_device_price, "Prices are not equals"
        #logging.INFO('Test was successful')
        logger.info("Test was successful")
        if os.path.exists(os.path.join(os.getcwd(), 'output')):
            shutil.rmtree(os.path.join(os.getcwd(), 'output'))

        os.mkdir('output')
