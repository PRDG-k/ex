# import asyncio

from utils.crawling_libs import *


task1 = {"id": "a1",
        "url": "https://m.etnews.com/",
        "wait_condition": EC.presence_of_all_elements_located((By.CSS_SELECTOR, "main")),
        "parser": parse_articles,
        "action": None}

task2 = {"id": "s1",
        "url": "https://finance.naver.com/marketindex/",
        "wait_condition": EC.presence_of_all_elements_located((By.CSS_SELECTOR, "body")),
        "parser": parse_exchange_rate,
        "action": None}

task3 = {"id": "s2",
        "url": "https://finance.naver.com/item/main.naver?code=005930",
        "wait_condition": EC.presence_of_all_elements_located((By.CSS_SELECTOR, "body")),
        "parser": parse_stock_info,
        "action": None}

async def main():
    articles, exchange, stock = await asyncio.gather(
        async_crawl(task1),
        async_crawl(task2),
        async_crawl(task3)
    )
    print(stock)

asyncio.run(main())