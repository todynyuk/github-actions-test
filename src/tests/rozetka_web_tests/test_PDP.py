import time
from pages.device_page import DevicePage
from pages.devices_category_page import DeviceCategory
from pages.main_page import MainPage
from pages.sub_category_page import SubCategory
import time,os,sys

class TestDetailsPage:
    def testItemRamAndPrice(self):
        main_page = MainPage('https://rozetka.com.ua/ua/')
        main_page.open()
        time.sleep(2)
        print("This is standard print test")
        main_page.click_universal_category_link("Смартфони")
        time.sleep(2)
        SubCategory.click_universal_subcategory_menu_link(self, "Мобільні")
        time.sleep(2)
        DeviceCategory.choose_ram_сapacity(self,12)
        DeviceCategory.click_check_box_filter(self,"Синій")
        smartphone_price = DeviceCategory.getSmartphonePriceText(self,1)
        DeviceCategory.clickLinkMoreAboutDevice(self,1)
        time.sleep(2)
        short_characteristics = DevicePage.verify_device_short_characteristic(self,12)
        chosen_device_price = DevicePage.get_chosen_product_price(self,)
        assert short_characteristics, "Short_characteristics don't contains chosen ram capacity"
        assert str(smartphone_price) == chosen_device_price, "Prices are not equals"
        if os.path.exists(os.path.join(os.getcwd(), 'output')):
            shutil.rmtree(os.path.join(os.getcwd(), 'output'))
        os.mkdir('output')
        time.sleep(2)
