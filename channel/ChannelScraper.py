from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from fake_useragent import UserAgent
import time

class ChannelScraper:
    def __init__(self, query):
        self.YOUTUBE = "https://www.youtube.com/"
        self.RESULT = f"https://www.youtube.com/results?search_query={query}&sp=EgIQAg%253D%253D"
        self.browser = self.start_browser()
        self.wait = WebDriverWait(self.browser, 30)
        self.check_browser_update()
        self.click_channel()
    
    def start_browser(self):
        # headless option needed 
        # options = webdriver.ChromeOptions()
        options = webdriver.FirefoxOptions()
        ua = UserAgent()
        userAgent = ua.random
        options.add_argument(f'user-agent={userAgent}')
        options.add_argument("start-maximized")
        profile = webdriver.FirefoxProfile("/Users/bbq12340/Library/Application Support/Firefox/Profiles")
        PROXY_HOST = "12.12.12.123"
        PROXY_PORT = "1234"
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", PROXY_HOST)
        profile.set_preference("network.proxy.http_port", int(PROXY_PORT))
        profile.set_preference("dom.webdriver.enabled", False)
        profile.set_preference('useAutomationExtension', False)
        profile.update_preferences()
        desired = webdriver.DesiredCapabilities.FIREFOX

        # options.add_experimental_option("useAutomationExtension", False)
        # options.add_experimental_option("excludeSwitches", list("enable-automation"))
        # browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        # browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        browser = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired)
        browser.get(self.YOUTUBE)
        return browser
    
    def check_browser_update(self):
        try:
            update_notice = self.browser.find_element_by_xpath("//*[contains(text(), '브라우저를 업데이트하세요.')]")
            pass_btn = self.browser.find_element_by_id("return-to-youtube")
            pass_btn.click()
        except NoSuchElementException:
            pass
        return
    
    def click_channel(self):
        channels = self.browser.find_elements_by_id("info-section")
        c = channels[0]
        c.click()
