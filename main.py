from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from time import time, sleep

site_fast = 'https://fast.com/'
site_twitter = 'https://twitter.com/'
email = 'epbfpm@gmail.com'
pwd = '^pf3ed+j=B%TAth'


# selenium setup
chrome_driver = "G:/My Drive/Programming/z - tools/chromedriver.exe"

# keep window open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# start selenium
class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver):
        self.drivert = webdriver.Chrome(options=chrome_options, service=Service(chrome_driver))

        self.driver = webdriver.Chrome(service=Service(chrome_driver))
        self.up = 0
        self.down = 0

    def get_internet_speed(self, site):
        self.driver.get(url=site)
        sleep(10)
        self.down = self.driver.find_element(By.ID, "speed-value").text
        print('down')
        print(self.down)
        self.driver.find_element(By.ID, 'show-more-details-link').click()
        sleep(10)
        self.up = self.driver.find_element(By.ID, "upload-value").text
        print('up')
        print(self.up)

    def tweet_at_provider(self, site):
        self.drivert.get(url=site)
        sleep(5)
        self.drivert.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div[1]/a/div/span/span').click()
        sleep(5)
        login = self.drivert.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        login.click()
        login.send_keys(email)
        login.send_keys(Keys.ENTER)
        sleep(5)
        try:
            login = self.drivert.find_element(By.XPATH,
                                          '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            login.click()
            login.send_keys(pwd)
            login.send_keys(Keys.ENTER)
        except NoSuchElementException:


        # input = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div''[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/''div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        # input.send_keys(f'Hey! My download speed is {self.down} and my upload speed is {self.up}')
        # input = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span').click()


bot = InternetSpeedTwitterBot(chrome_driver)
# bot.get_internet_speed(site_fast)
bot.tweet_at_provider(site_twitter)
