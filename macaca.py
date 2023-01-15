from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from time import time, sleep
from selenium.webdriver.chrome.options import Options
from random import choice
import smtplib as sm

# ======================= constants ====================== #
site_fast = 'https://fast.com/'
site_twitter = 'https://twitter.com/'
email = 'epbfpm@gmail.com'
pwd = '^pf3ed+j=B%TAth'
user = 'epbfpm'
chrome_driver = "G:/My Drive/Programming/z - tools/chromedriver.exe"
receiver = 'matmourase@gmail.com'
receiver2 = "meucu@gmail.com"
smtp, gmail, pwd2 = 'smtp.gmail.com', 'elder.estuda.voce.recebe.email@gmail.com', 'ndwhhxioybtizozb'

# =================== keep window open =================== #
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# ======================= functions ======================= #
class TwitterBot:
    def __init__(self, chrome_driver):
        self.driver = webdriver.Chrome(options=chrome_options, service=Service(chrome_driver))
        self.up = 0
        self.down = 0
        self.frase_de_hoje = ''
        self.frases = []

    def choose_phrase(self):
        # == == == == == == == == == == == = frases == == == == == == == == == == == == =  #
        try:
            with open('txt.txt', encoding='utf-8') as data:
                self.frases = data.readlines()
                self.frase_de_hoje = choice(self.frases)
                self.frases.remove(self.frase_de_hoje)

            with open("txt.txt", "w", encoding='utf-8') as f:
                for line in self.frases:
                    f.write(line)
            print(self.frase_de_hoje)
        except IndexError:
            self.frase_de_hoje = ('Foi um prazer desmotivá-lo. Já estou com saudades')
            pass
        # self.frase_de_hoje = "@matmourase Mensagem desmotivacional 3/30: Motivação faz você começar e o hábito faz você DESISTIR."

    def tweet(self, site):
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
        login = self.driver.find_element(By.XPATH,
                                         '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        login.click()
        login.send_keys(email)
        login.send_keys(Keys.ENTER)
        sleep(2)

        try:
            # ================= try to input password ================ #
            login = self.driver.find_element(
                By.XPATH,
                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            login.click()
            login.send_keys(pwd)
            login.send_keys(Keys.ENTER)
        except NoSuchElementException:
            # ============= pass strange behaviour prompt ============ #
            login = self.driver.find_element(
                By.XPATH,
                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            login.click()
            login.send_keys(user)
            login.send_keys(Keys.ENTER)
            # ==================== input password ==================== #
            sleep(2)
            login = self.driver.find_element(
                By.XPATH,
                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
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
            msg = f'@matmourase Mensagem desmotivacional {30 - len(self.frases)}/30: {self.frase_de_hoje}'
            input.send_keys(
                msg)
            input = self.driver.find_element(
                By.XPATH,
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span').click()
            ok = False
            self.send(msg)

    def run(self):
        self.choose_phrase()
        self.tweet(site_twitter)

    def send(self, msg):
        with sm.SMTP(smtp, port=587) as mail:
            mail.starttls()
            mail.login(user=gmail, password=pwd2)
            mail.sendmail(from_addr=gmail, to_addrs=receiver, msg=f'Subject: Desmotive-se!\n\n{msg.encode("utf-8")}')
            print(msg)


bot = TwitterBot(chrome_driver)
bot.run()
# msg = '@matmourase Mensagem desmotivacional 5/30: Cabe a você escolher aquilo de lhe aflige.'
# bot.send(msg)