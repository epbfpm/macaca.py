from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from time import time, sleep
from selenium.webdriver.chrome.options import Options

# ======================= constants ====================== #
site_fast = 'https://fast.com/'
site_twitter = 'https://twitter.com/'
email = 'epbfpm@gmail.com'
pwd = '^pf3ed+j=B%TAth'
user = 'epbfpm'
chrome_driver = "G:/My Drive/Programming/z - tools/chromedriver.exe"

# =================== keep window open =================== #
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# ======================= functions ======================= #


class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver):
        self.driver = webdriver.Chrome(
            options=chrome_options, service=Service(chrome_driver))
        self.up = 0
        self.down = 0

    def get_internet_speed(self, site):
        self.driver.get(url=site)
        sleep(10)
        # ================== get download speed ================== #
        self.down = self.driver.find_element(By.ID, "speed-value").text
        self.driver.find_element(By.ID, 'show-more-details-link').click()
        sleep(10)
        # =================== get upload speed =================== #
        self.up = self.driver.find_element(By.ID, "upload-value").text

    def tweet_at_provider(self, site):
        # ======================================================== #
        #                     LOGIN TO TWITTER                     #
        # ======================================================== #
        self.driver.get(url=site)
        sleep(2)
        # ====================== click login ===================== #
        self.driver.find_element(By.XPATH,
                                 '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div[1]/a/div/span/span').click()
        sleep(2)
        # ================ click sign in with emal =============== #
        login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        login.click()
        login.send_keys(email)
        login.send_keys(Keys.ENTER)
        sleep(2)
        try:
            # ================= try to input password ================ #
            login = self.driver.find_element(
                By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            login.click()
            login.send_keys(pwd)
            login.send_keys(Keys.ENTER)
        except NoSuchElementException:
            # ============= pass strange behaviour prompt ============ #
            login = self.driver.find_element(
                By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            login.click()
            login.send_keys(user)
            login.send_keys(Keys.ENTER)
            # ==================== input password ==================== #
            sleep(2)
            login = self.driver.find_element(
                By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            login.click()
            login.send_keys(pwd)
            login.send_keys(Keys.ENTER)

            # ======================================================== #
            #                       actualy tweet                      #
            # ======================================================== #
            sleep(2)
            input = self.driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Tweet text')]")
            input.click()
            sleep(1)
            input.send_keys(
                f'@matmourase Hey! My download speed is {self.down} and my upload speed is {self.up}')
            input = self.driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span').click()


bot = InternetSpeedTwitterBot(chrome_driver)
bot.get_internet_speed(site_fast)
bot.tweet_at_provider(site_twitter)
