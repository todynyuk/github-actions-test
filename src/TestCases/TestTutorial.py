from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time,os,shutil

def test_tutorial():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),chrome_options=options)
    driver.get("https://www.whatismybrowser.com/")
    driver.maximize_window()
    time.sleep(5)
    print("browser opened")
    print(os.getcwd())
    if os.path.exists(os.path.join(os.getcwd(),'output')):
        shutil.rmtree(os.path.join(os.getcwd(),'output'))

    os.mkdir('output')
    driver.save_screenshot('output/screen.png')
    driver.close()