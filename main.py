from playwright.sync_api import sync_playwright
from urllib.request import urlretrieve
import time
import os
import random
import sys
url = input("Wpisz url slajdszoła:")
def download(url):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://ttsave.app/en/slide")

    page.wait_for_load_state("networkidle")

    page.locator('body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button > p').click()
    page.locator('#input-query').fill(url)
    page.locator("#btn-download").click()

    #get the url of button
    # url1 = page.locator("#button-download-ready > a:nth-child(2)").get_attribute("href")
    # print(url1)
    # url2 = page.locator("#button-download-ready > a:nth-child(4)").get_attribute("href")
    # print(url2)

    time.sleep(3)