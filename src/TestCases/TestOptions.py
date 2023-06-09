from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time,os,shutil
import logging

def test_options():
    #'%(asctime)s - %(levelname)s - %(message)s'
    #logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logger = logging.getLogger('example_logger')
    logger.warning('This is a warning')
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    #logging.info("browser opened")
    #logging.info('Opening the page...')
    print("Test Print Function In Logs Artifact")
    driver.get("https://www.whatismybrowser.com/")
    driver.maximize_window()
    time.sleep(5)
    print("================Check loggin start======================")
    logging.info(os.getcwd())
    print("================Check loggin finish======================")
    if os.path.exists(os.path.join(os.getcwd(), 'output')):
        shutil.rmtree(os.path.join(os.getcwd(), 'output'))

    os.mkdir('output')
    driver.save_screenshot('output/screen.png')
    driver.close()
