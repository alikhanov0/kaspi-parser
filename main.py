import requests
from bs4 import BeautifulSoup

st_accept = "text/html"

st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}

req = requests.get("https://kaspi.kz/shop/c/smartphones/?q=%3AavailableInZones%3AMagnum_ZONE1%3Acategory%3ASmartphones%3ASmartphones*Series%3AApple%20iPhone%2017%20Pro%20Max&sort=relevance&sc=", headers=headers)

src = req.text

soup = BeautifulSoup(src, "lxml")

print(req.status_code)

print("item-card__prices-price" in src)

ans = soup.find("span", class_="item-card__prices-price")

print(ans)