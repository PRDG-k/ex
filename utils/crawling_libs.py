import requests
import asyncio

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement

from concurrent.futures import ThreadPoolExecutor

def get_html(url):
    response = requests.get(url)
    html = bs(response.text, 'html.parser')
    return html

async def async_quit(driver: ChromeDriverManager, t: int):
    await asyncio.sleep(t)
    driver.quit()

# 공통 Selenium 실행 함수
CHROMEDRIVER_PATH = ChromeDriverManager().install()
def run_crawler_task(task: dict):
    service = Service(CHROMEDRIVER_PATH)

    url = task['url']
    wait_condition = task['wait_condition']  # WebDriverWait에 넘길 조건
    parser = task['parser']  # BeautifulSoup or selenium-parsing 함수
    # action = task['action']

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)

        if wait_condition:
            WebDriverWait(driver, 10).until(wait_condition)

        return parser(driver)
    finally:
        driver.quit()

# 비동기 래퍼
async def async_crawl(task):
    loop = asyncio.get_event_loop()
    print(f"Task {task['id']} start")
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, run_crawler_task, task)
        print(f"Task {task['id']} finished")
    return result

def parse_articles(driver: webdriver.Chrome):
    from itertools import chain
    # href 수집
    lank9_urls = [e.get_attribute("href") for e in driver.find_elements(By.CSS_SELECTOR, ".lank9 h2 a")]
    related_urls = [e.get_attribute("href") for e in driver.find_elements(By.CSS_SELECTOR, ".lank9 .related a")]
    lank8_urls = [e.get_attribute("href") for e in driver.find_elements(By.CSS_SELECTOR, ".lank8 a")]

    all_urls = list(chain(lank9_urls, related_urls, lank8_urls))

    articles = []
    for url in all_urls:
        driver.get(url)
        print(f"Moving to {url}...")

        title = driver.find_element(By.CSS_SELECTOR, "#article_title_h2").text
        date = driver.find_element(By.CSS_SELECTOR, "div.time").text
        content = driver.find_element(By.CSS_SELECTOR, "div.article_body p").text

        articles.append({
            "title": title,
            "date": date,
            "content": "".join(content.split("\n"))
        })

    return articles

def parse_exchange_rate(driver: webdriver.Chrome):
    country = [e.get_attribute("innerText") for e in driver.find_elements(By.CSS_SELECTOR, "div.market1 h3")]
    exchange_rates = [e.text for e in driver.find_elements(By.CSS_SELECTOR, "div.market1 span.value")]

    result = dict(zip(country, exchange_rates))
    return result

def parse_stock_info(driver: webdriver.Chrome):
    sise = driver.find_element(By.CSS_SELECTOR, ".tabs_submenu .tab2")
    sise.click()

    columns = [e.text for e in driver.find_elements(By.CSS_SELECTOR, ".type_tax .title")]
    contents = [e.text for e in driver.find_elements(By.CSS_SELECTOR, ".type_tax td.num")]
    
    result = dict(zip(columns, contents))
    return result