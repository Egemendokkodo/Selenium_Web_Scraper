import sys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


class CryptoJobs:  # https://cryptojobslist.com/
    def __init__(self):

        self.options = webdriver.ChromeOptions()
        self.options.headless = True  # selenium browser kapatmak için bu özelliği True işaretlemek zorundayız.
        self.driver = webdriver.Chrome(options=self.options)

    def goToSite(self, url, page):
        self.driver.get(f"{url}{page}")
        button_elementss = self.driver.find_elements(By.XPATH, '//a[@role="button"]')

        for i in range(0, len(button_elementss)):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            button_elements = self.driver.find_elements(By.XPATH, '//a[@role="button"]')
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@role="button"]')))
            button_elements[i].click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[1]/div[1]/h1')))
            job_title_element = wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[1]/div[1]/h1')))
            title = job_title_element.text
            job_where_element = wait.until(EC.presence_of_element_located(
                (By.XPATH, '// *[ @ id = "__next"] / main / div[1] / div[1] / div[2] / h2 / span / span[1] / a')))
            where = job_where_element.text
            job_desc_element = wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[4]/div[1]/div[2]')))
            desc = job_desc_element.text
            self.write_to_file(title, desc, self.driver.current_url, where)
            time.sleep(0.45)
            self.driver.back()
            time.sleep(0.45)
            wait.until(EC.presence_of_element_located((By.XPATH, '//a[@role="button"]')))
        self.driver.quit()

    def write_to_file(self, title, desc, link, where):
        with open("Data/crypto_jobs.txt", "r", encoding="utf-8") as f:
            if desc in f.read():
                print(f"\n\nhttps://cryptojobslist.com/ İÇİN YENİ BİR İLAN YOK.")
                self.driver.quit()
                second_website()
                return

        with open("Data/crypto_jobs.txt", "a", encoding="utf-8") as f:
            f.write(f"Title: {title}\n")
            f.write(f"Description: {desc}\n")
            f.write(f"Link: {link}\n")
            f.write("--------------------------\n")
            print("------------------------------- YENİ HABERLERİNİZ MEVCUT--------------------")
            print(f"------------İLAN BAŞLIĞI ----------------\n")
            print(title + " at " + where + "\n")
            print(f"------------İLAN BAŞLIĞI SONU ----------------\n")
            print(f"------------İLAN AÇIKLAMASI ----------------\n")
            print(desc + "\n")
            print("İLANIN LİNKİ ::::::: " + self.driver.current_url)
            print(f"------------İLAN AÇIKLAMASI SONU ----------------\n")
            return


class Web3Jobs: # https://crypto.jobs/
    def __init__(self):

        self.options = webdriver.ChromeOptions()
        self.options.headless = True  # selenium browser kapatmak için bu özelliği True işaretlemek zorundayız.
        self.driver = webdriver.Chrome(options=self.options)

    def goToSite(self, url, page):
        self.driver.get(f"{url}{page}")

        button_elementss = self.driver.find_elements_by_xpath(
            '//td//a//p')

        for i in range(len(button_elementss)):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//td//a//p')))
            button_elements = self.driver.find_elements(By.XPATH, '//td//a//p')
            button_elements[i].click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//div//h3')))
            job_title_element = wait.until(
                EC.presence_of_element_located((By.XPATH, '//div//h3')))
            title = job_title_element.text
            job_desc_element = wait.until(
                EC.presence_of_element_located((By.XPATH, '//div//div/div/p')))
            desc = job_desc_element.text
            self.write_to_file(title, desc, self.driver.current_url)
            time.sleep(0.45)
            self.driver.back()
            time.sleep(0.45)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[1]/table/tbody/tr[3]')))

    def write_to_file(self, title, desc, link):
        with open("Data/web3_jobs.txt", "r", encoding="utf-8") as f:
            if desc in f.read():
                print(f"\n\nhttps://crypto.jobs/ İÇİN YENİ BİR İLAN YOK.")
                self.driver.quit()
                Web3Career().goToSite("https://web3.career/?page=", 1)
                return

        with open("Data/web3_jobs.txt", "a", encoding="utf-8") as f:
            f.write(f"Title: {title}\n")
            f.write(f"Description: {desc}\n")
            f.write(f"Link: {link}\n")
            f.write("--------------------------\n")
            print("------------------------------- YENİ HABERLERİNİZ MEVCUT--------------------")
            print(f"------------İLAN BAŞLIĞI ----------------\n")
            print(title)
            print(f"------------İLAN BAŞLIĞI SONU ----------------\n")
            print(f"------------İLAN AÇIKLAMASI ----------------\n")
            print(desc + "\n")
            print("İLANIN LİNKİ ::::::: " + self.driver.current_url)
            print(f"------------İLAN AÇIKLAMASI SONU ----------------\n")
            return


class Web3Career: #https://web3.career/


    def goToSite(self, url, page):
        import requests
        from lxml import etree, html

        url = "https://web3.career/api/v1.xml?token=rAn8w1DNWP9Gw2jks6uPiuuMjy7y7Ga8"

        response = requests.get(url)

        root = etree.fromstring(response.content)

        for item in root.findall("./channel/item"):
            title = item.find("title").text
            apply_url = item.find("link").text
            description = item.find("description").text
            if description is not None:
                description_html = html.fromstring(description)
                description_text = description_html.text_content()
            else:
                description_text = "N/A"
            self.write_to_file(title, apply_url, description_text)
            print(f"Title: {title}\nApply URL: {apply_url}\nDescription: {description_text}\n")

    def write_to_file(self, title, desc, link):
        with open("Data/web3_career.txt", "r", encoding="utf-8") as f:
            if link in f.read():
                print(f"\n\nhttps://web3.career/ İÇİN YENİ BİR İLAN YOK.")
                sys.exit()

        with open("Data/web3_career.txt", "a", encoding="utf-8") as f:
            f.write(f"Title: {title}\n")
            f.write(f"Description: {desc}\n")
            f.write(f"Link: {link}\n")
            f.write("--------------------------\n")
            print("------------------------------- YENİ HABERLERİNİZ MEVCUT--------------------")
            print(f"------------İLAN BAŞLIĞI ----------------\n")
            print(title)
            print(f"------------İLAN BAŞLIĞI SONU ----------------\n")
            print(f"------------İLAN AÇIKLAMASI ----------------\n")
            print(desc + "\n")
            print("İLANIN LİNKİ ::::::: " + link)
            print(f"------------İLAN AÇIKLAMASI SONU ----------------\n")


def first_website():
    for i in range(1, 20, 1):
        CryptoJobs().goToSite("https://cryptojobslist.com/?page=", i)


def second_website():
    for i in range(1, 20, 1):
        Web3Jobs().goToSite("https://crypto.jobs/?page=", i)


first_website()

