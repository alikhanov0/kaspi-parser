import requests
from bs4 import BeautifulSoup

url = "https://kaspi.kz/yml/product-view/pl/results"



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://kaspi.kz/shop/",
    "X-KS-City": "750000000",
}

for i in (1,100):

    params = {
        "page": str(i),
        "q": ":availableInZones:Magnum_ZONE1:category:Smartphones:Smartphones*Series:Apple iPhone 17 Pro Max",
        "text": "",
        "sort": "relevance",
        "qs": "",
        "requestId": "7e4b87a629a9c20118c66e3de410251e",
        "ui": "d",
        "i": "-1",
        "c": "750000000"
    }

    response = requests.get(url, params=params, headers=headers, timeout=10)

    data = response.json()
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list):
            products = data
        elif isinstance(data, dict):
            products = data.get("cards") or data.get("data") or data.get("results") or []
        else:
            products = []

        for item in products:
            if isinstance(item, dict):
                price = item.get("unitPrice")

                if (price > 800000):
                    continue

                title = item.get("title")
                merchant = item.get("bestMerchant")
                rating = item.get("rating")
                shop_link = item.get("shopLink", "")
                link = f"https://kaspi.kz{shop_link}" if shop_link else "Нет ссылки"
                
                print(f"Товар: {title}")
                print(f"Цена: {price} ₸")
                print(f"Продавец: {merchant}")
                print(f"Рейтинг: {rating}")
                print(f"Ссылка: {link}")
                print("-" * 40)
    else:
        print(f"Ошибка запроса: статус {response.status_code}")