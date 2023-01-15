from time import time, sleep
from random import choice
import smtplib as sm

# ======================= constants ====================== #
site_fast = 'https://fast.com/'
chrome_driver = "G:/My Drive/Programming/z - tools/chromedriver.exe"
receiver = 'matmourase@gmail.com'
smtp, gmail, pwd2 = 'smtp.gmail.com', 'elder.estuda.voce.recebe.email@gmail.com', 'ndwhhxioybtizozb'

# ======================= functions ======================= #
class DownBot:
    def __init__(self):
        self.frase_de_hoje = ''
        self.frases = []

    def choose_phrase(self):
        # == == == == == == == == == == == = frases == == == == == == == == == == == == =  #
        try:
            with open('txt.txt', encoding='utf-8') as data:
                self.frases = data.readlines()
                self.frase_de_hoje = choice(self.frases)
                self.frases.remove(self.frase_de_hoje)

            print(self.frase_de_hoje)
        except IndexError:
            self.frase_de_hoje = ('Foi um prazer desmotivá-lo. Já estou com saudades')
            pass
        # self.frase_de_hoje = "@matmourase Mensagem desmotivacional 3/30: Motivação faz você começar e o hábito faz você DESISTIR."

    def run(self):
        self.choose_phrase()
        self.send()

    def send(self):
        msg = f'@matmourase Mensagem desmotivacional {30 - len(self.frases)}/30: {self.frase_de_hoje}'
        with sm.SMTP(smtp, port=587) as mail:
            mail.starttls()
            mail.login(user=gmail, password=pwd2)
            mail.sendmail(from_addr=gmail, to_addrs=receiver, msg=(f'Subject: Desmotive-se!\n\n{msg}'.encode("utf-8")))
            print(msg)
        with open("txt.txt", "w", encoding='utf-8') as f:
            for line in self.frases:
                f.write(line)


bot = DownBot()
bot.run()
