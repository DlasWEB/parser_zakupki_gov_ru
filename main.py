#!/usr/bin/python3.9

import re
import requests
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent
import os
import datetime

useragent = UserAgent()
urls_list = []
absolute_path_to_folder_with_script = '/home/fj/PycharmProjects/parser_zakupki_gov_ru/'
with open(f"{absolute_path_to_folder_with_script}urls.txt", "r") as file:
    for line in file:
        urls_list.append(line.replace("\n", ""))
    file.close()

def get_data_selenium():
    count = 0
    for urls in urls_list:
        count += 1
        options = webdriver.ChromeOptions()
        options.add_argument(f"useragent={useragent.random}")
        options.headless = True
        try:
            driver = webdriver.Chrome(executable_path=f"{absolute_path_to_folder_with_script}chromedriver/chromedriver", options=options)
            driver.get(url=urls)
            time.sleep(4)
            with open("data/index_selenium.html", "w") as file:
                file.write(driver.page_source)
            time.sleep(5)
            with open("data/index_selenium.html") as file:
                soup = BeautifulSoup(file.read(), 'lxml')
                number_of_auction = soup.find("span", class_="cardMainInfo__purchaseLink distancedText").text.replace('№', '').strip()
                object_of_auction = soup.find("span", class_="cardMainInfo__content").text.strip()
                a_place_of_auction = soup.find("div", class_="row blockInfo").find("a").text.strip()
                part_price_of_auction = soup.find("div", class_="price").find("span", class_="cardMainInfo__title").text.strip()
                price_of_auction = soup.find("div", class_="price").find("span", class_="cardMainInfo__content cost").text.replace("\u00A0", "").strip()
                part_application_of_auction = "Обеспечение заявки"
                try:
                    application_of_auction = soup.find("div", id="custReqNoticeTable").find("h2", text="Обеспечение заявки").find_next().find_next().find_next().find_next().find("span", class_="section__info").text.replace("\u00A0", "").strip()
                except Exception:
                    application_of_auction = " "
                part_contract_of_auction = "Обеспечение исполнения контракта"
                try:
                    contract_of_auction = soup.find("div", id="custReqNoticeTable").find("h2", text="Обеспечение исполнения контракта").find_next_sibling().find_next_sibling().find("span", class_="section__info").text.replace("\u00A0", "").strip()
                except:
                    contract_of_auction = ""
                part_guarantees_of_auction = "Обеспечение гарантийных обязательств"
                try:
                    guarantees_of_auction = soup.find("div", id="custReqNoticeTable").find("h2", text="Обеспечение гарантийных обязательств").find_next().find_next().find_next().find_next().find_next().find_next().text.replace(
                        "\u00A0", "").strip()
                except Exception:
                    guarantees_of_auction = ""
                try:
                    deliver_auction = soup.find("h2", text="Условия контракта").find_parent().find("span", class_="section__title", text=re.compile("Сроки")).find_next().text.strip()
                except Exception:
                    deliver_auction = ""
                try:
                    place_deliver_auction = soup.find("h2", text="Условия контракта").find_parent().find("span", class_="section__title", text=re.compile("Место")).find_next().text.strip()
                except Exception:
                    place_deliver_auction = ""
                try:
                    date_of_last_open_auction = soup.find("span", class_="section__title", text="Дата и время окончания срока подачи заявок").find_next().text.replace(
                        "\u00A0", "").strip()
                except Exception:
                    date_of_last_open_auction = soup.find("span", class_="section__title", text="Дата и время начала срока подачи заявок").find_next().text.strip()
                data_of_auction_list = []
                data_of_auction_list.insert(0, number_of_auction + " " + object_of_auction + " " + a_place_of_auction)
                data_of_auction_list.insert(1, part_price_of_auction + " " + price_of_auction)
                data_of_auction_list.insert(2, part_application_of_auction + " " + application_of_auction)
                data_of_auction_list.insert(3, part_contract_of_auction + " " + contract_of_auction)
                data_of_auction_list.insert(4, part_guarantees_of_auction + " " + guarantees_of_auction)
                data_of_auction_list.insert(5, "Срок поставки" + " " + deliver_auction)
                data_of_auction_list.insert(6, "Срок оплаты 10")
                data_of_auction_list.insert(7, "Дата подачи" + " " + date_of_last_open_auction)
                data_of_auction_list.insert(8, "Место" + " " + place_deliver_auction)
                os.remove(f"{absolute_path_to_folder_with_script}data/index_selenium.html")
                new_name = number_of_auction
                os.mkdir(f"{absolute_path_to_folder_with_script}data/{new_name}")
                with open(f"{absolute_path_to_folder_with_script}data/{new_name}/{new_name}.docx", "w", encoding="UTF-8") as file:
                    for item in data_of_auction_list:
                        file.write(item + "\n")
            time.sleep(13)
            driver.get(url=urls)
            driver.implicitly_wait(4)
            driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div[1]/div[3]/div/a[2]").click()
            driver.implicitly_wait(4)
            driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div[2]/div/label/span[1]").click()
            driver.implicitly_wait(4)
            with open("data/index_doc_selenium.html", "w") as file:
                file.write(driver.page_source)
            with open("data/index_doc_selenium.html") as file:
                soup = BeautifulSoup(file.read(), 'lxml')
                number_of_auction_1 = soup.find("span", class_="cardMainInfo__purchaseLink distancedText").text.replace('№', '').strip()
                doc_0 = soup.find("h2", class_="blockInfo__title").find_all_next(href=re.compile("download"))
                clear_urls_list = []
                for links in doc_0:
                    clean_urls = links.get("href")
                    clear_urls_list.append(clean_urls)
                for clear_urls in clear_urls_list:
                    driver.get(url=clear_urls)
                    driver.implicitly_wait(7)
            time.sleep(2)
            os.remove(f"{absolute_path_to_folder_with_script}data/index_doc_selenium.html")
            new_name_1 = number_of_auction_1
            source_path = absolute_path_to_folder_with_script
            destination_path = f"{absolute_path_to_folder_with_script}data/{new_name_1}/"
            files = os.listdir(source_path)
            files_for_remove = ['urls.txt', 'venv', 'chromedriver', 'main.py', 'data', '.idea', 'README.md', '.gitignore', 'LICENSE']
            for i in files_for_remove:
                files.remove(i)
            for file in files:
                os.rename(source_path + file, destination_path + file)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()
        print(f"Сделано шапок {count} из {len(urls_list)}")

def main():
    start_time = datetime.datetime.now()
    print(f"Всего шапок: {len(urls_list)}")
    get_data_selenium()
    finish_time = datetime.datetime.now()
    print(f"Ср. время подготовки одной шапки: {(finish_time - start_time)/len(urls_list)} час(ов):минут(а):секунд(а)")
    print(f"Все шапки сделаны за {finish_time - start_time} час(ов):минут(а):секунд(а)")

if __name__ == '__main__':
    main()

