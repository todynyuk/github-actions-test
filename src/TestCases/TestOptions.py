from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time,os,shutil
import logging

def test_options():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("https://www.whatismybrowser.com/")
    driver.maximize_window()
    time.sleep(5)
    logging.info("browser opened")
    logging.info(os.getcwd())
    if os.path.exists(os.path.join(os.getcwd(), 'output')):
        shutil.rmtree(os.path.join(os.getcwd(), 'output'))

    os.mkdir('output')
    f_handler = logging.FileHandler('output/report.log')


    formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')

    f_handler.setFormatter(formatter)
    logger.addHandler(f_handler)
    driver.save_screenshot('output/screen.png')
    driver.close()
