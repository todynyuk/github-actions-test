from selenium import webdriver

HOST = "localhost"

def test_firefox():
    capabilities = {
        "browserName": "firefox",
        "version": "108.0",
        "enableVNC": False,
        "enableVideo": False
    }
    firefox = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST),
                               desired_capabilities=capabilities)
    firefox.get('https://www.google.com')
    print('firefox', firefox.title)
    title=firefox.title
    assert title=="Google", "Title not are Google"
    firefox.quit()

def test_chrome():
    capabilities = {
        "browserName": "chrome",
        "version": "108.0_VNC",
        "enableVNC": True,
        "enableVideo": False
    }
    chrome = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST),
                              desired_capabilities=capabilities)
    chrome.get('https://www.google.com')
    print('chrome', chrome.title)
    assert title=="Google", "Title not are Google"
    chrome.quit()


if __name__ == "__main__":
    test_firefox()
    test_chrome()
